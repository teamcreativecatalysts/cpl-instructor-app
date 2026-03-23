import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from openai import AzureOpenAI
import json
from pathlib import Path
import pyodbc

app = Flask(__name__, template_folder="templates")

# ===============================
# Load data files
# ===============================
BASE_DIR = Path(__file__).resolve().parent

try:
    POLICY_DIGEST = (BASE_DIR / "data" / "policy_digest.md").read_text(encoding="utf-8")
except Exception as e:
    POLICY_DIGEST = "Policy digest unavailable."
    app.logger.warning(f"Could not load policy_digest.md: {e}")

try:
    INTERVIEW_SCHEMA = json.loads(
        (BASE_DIR / "data" / "interview_schema.json").read_text(encoding="utf-8")
    )
except Exception as e:
    INTERVIEW_SCHEMA = {}
    app.logger.warning(f"Could not load interview_schema.json: {e}")

# ===============================
# Build system prompt
# ===============================
def build_system_prompt():
    return f"""
You are a PLA (Prior Learning Assessment) intake assistant for Northeastern University College of Professional Studies.
Your job is to run a structured interview and collect evidence for human evaluation.

IMPORTANT RULES:
- Ask one question at a time.
- Be structured and formal.

POLICY DIGEST:
{POLICY_DIGEST}

DATA TO COLLECT:
{json.dumps(INTERVIEW_SCHEMA, indent=2)}
""".strip()

# ===============================
# Azure OpenAI Client
# ===============================
def get_client():
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview")

    if not endpoint:
        return None, "Missing AZURE_OPENAI_ENDPOINT"
    if not api_key:
        return None, "Missing AZURE_OPENAI_API_KEY"

    try:
        client = AzureOpenAI(
            azure_endpoint=endpoint,
            api_key=api_key,
            api_version=api_version,
        )
        return client, None
    except Exception as e:
        return None, str(e)

# ===============================
# DB Save Function
# ===============================
def save_session_to_db(nuid, student_name, scenario, conversation_log):
    conn_str = os.getenv("SQL_CONNECTION_STRING")
    if not conn_str:
        app.logger.warning("SQL_CONNECTION_STRING not set")
        return

    try:
        conn = pyodbc.connect(conn_str, timeout=10)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO pla_sessions (nuid, student_name, scenario, conversation_log)
            VALUES (?, ?, ?, ?)
        """, nuid, student_name, scenario, json.dumps(conversation_log))

        conn.commit()
        conn.close()

        app.logger.info("Saved to DB")

    except Exception as e:
        app.logger.exception(f"DB ERROR: {e}")

# ===============================
# Routes
# ===============================
@app.get("/")
def home():
    return render_template("index.html")

@app.get("/chat")
def chat_page():
    return render_template("chat.html")

@app.get("/admin")
def admin_page():
    return render_template("admin.html", status={
        "SQL_CONNECTION_STRING": "✅ set" if os.getenv("SQL_CONNECTION_STRING") else "❌ missing"
    })

@app.get("/dbcheck")
def dbcheck():
    try:
        conn = pyodbc.connect(os.getenv("SQL_CONNECTION_STRING"), timeout=10)
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ===============================
# CHAT ENDPOINT (FIXED)
# ===============================
@app.post("/api/chat")
def api_chat():
    try:
        data = request.get_json() or {}
        user_message = (data.get("message") or "").strip()

        if not user_message:
            return jsonify({"error": "Message required"}), 400

        client, err = get_client()
        if err:
            return jsonify({"error": err}), 500

        deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

        history = data.get("history") or []

        safe_history = [
            {"role": h["role"], "content": h["content"]}
            for h in history
            if isinstance(h, dict)
        ]

        response = client.chat.completions.create(
            model=deployment,
            messages=[
                {"role": "system", "content": build_system_prompt()}
            ] + safe_history + [
                {"role": "user", "content": user_message}
            ],
            temperature=0.3
        )

        answer = (response.choices[0].message.content or "").strip()

        # ===============================
        # ✅ ALWAYS SAVE TO DB
        # ===============================
        session_meta = data.get("session_meta") or {}

        nuid = session_meta.get("nuid")
        student_name = session_meta.get("student_name")
        scenario = session_meta.get("scenario")

        full_history = safe_history + [
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": answer},
        ]

        save_session_to_db(
            nuid or "pending",
            student_name or "pending",
            scenario or "pending",
            full_history
        )

        return jsonify({"answer": answer})

    except Exception as e:
        app.logger.exception("Chat failed")
        return jsonify({"error": str(e)}), 500


# ===============================
# Run locally
# ===============================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
