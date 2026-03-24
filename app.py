import os
import base64
import tempfile
from flask import Flask, render_template, request, jsonify, send_from_directory
from openai import AzureOpenAI
import json
from pathlib import Path
import pyodbc


# Explicit template folder for Azure App Service reliability
app = Flask(__name__, template_folder="templates")

# ADDED — loads both data files at startup:
BASE_DIR = Path(__file__).resolve().parent
 
try:
    POLICY_DIGEST = (BASE_DIR / "data" / "policy_digest.md").read_text(encoding="utf-8")
except Exception as e:
    POLICY_DIGEST = "Policy digest unavailable."
    app.logger.warning(f"Could not load policy_digest.md: {e}")
 
try:
    INTERVIEW_SCHEMA = json.loads((BASE_DIR / "data" / "interview_schema.json").read_text(encoding="utf-8"))
except Exception as e:
    INTERVIEW_SCHEMA = {}
    app.logger.warning(f"Could not load interview_schema.json: {e}")

# Build system prompt
def build_system_prompt():
    return f"""
You are a PLA (Prior Learning Assessment) intake assistant for Northeastern University College of Professional Studies.
Your job is to run a structured interview and collect evidence for human evaluation.
 
NON-NEGOTIABLE RULES:
- Be formal.
- Be structured.
- Ask only one question at a time. Never ask two questions in the same message.
- Do not combine questions. Do not say "and also" or "while you're at it".
- Wait for the student to answer before moving to the next question.
- If you catch yourself about to ask a second question, stop and save it for the next turn.
- Follow the interview flow exactly. Do not skip or reorder steps.
- If the student provides a course code that clearly indicates the program area 
  (e.g., "ITC" prefix = Information Technology, "ALY" prefix = Analytics/Data Science), 
  do NOT ask which program area it belongs to. Infer it automatically from the course code 
  and move on. Only ask the program area question if the course prefix is ambiguous 
  (e.g., CHEM, ACC, CMN, or other non-ITC/ALY codes).

DOCUMENT COLLECTION RULES:
- When you reach the document checklist stage for any scenario, present documents ONE AT A TIME.
- For each document, ask if the student has it ready. If they say yes (or confirm), end your
  message with the exact token: [SHOW_UPLOAD:<document label>]
  Examples:
    [SHOW_UPLOAD:Resume]
    [SHOW_UPLOAD:Official Transcript]
    [SHOW_UPLOAD:HR Statement]
    [SHOW_UPLOAD:Portfolio Narrative]
    [SHOW_UPLOAD:Work Samples]
    [SHOW_UPLOAD:Certification Credential]
    [SHOW_UPLOAD:Course Syllabus]
- After the student uploads (or skips), move on to the next document.
- Never list all documents at once and never show [SHOW_UPLOAD] for a document the student
  said they don't have yet.
 
SCENARIO DETECTION APPROACH:
- After collecting NUID and name, ask the student to describe their background in their own words
  INSTEAD of immediately presenting a lettered menu.
- Listen for key signals in their answer:
    * "took courses / credits / enrolled at another school but didn't finish" -> likely Scenario A
    * "certification / CompTIA / AWS / PMP / bootcamp" -> likely Scenario B
    * "years of experience / work history / job responsibilities / industry background" -> likely Scenario C
    * "completed my degree / earned my master's / graduated from" -> likely NOT eligible (Scenario D)
- Based on those signals, name the scenario you believe applies and ASK THE STUDENT TO CONFIRM
  before proceeding. Example: "That sounds like Scenario C: Work Experience. To confirm — you're
  applying based on professional experience, not a certification or prior coursework. Is that right?"
- Only after confirmation, proceed with the matching question flow.
- If the student's description is ambiguous, ask one clarifying question to narrow it down.
  Do not guess — confirm first.
 
INTERVIEW FLOW:
1. Ask for the student's NUID (9-digit number). Validate it is exactly 9 digits. If not, ask again.
2. Ask for their full name.
3. Ask the user which program they are enrolled in.
4. Greet them by name and ask them to briefly describe what they are requesting CPL or PLA credit for
   (open-ended — do NOT present the A/B/C/D menu yet).
5. Based on their answer, identify the most likely scenario and CONFIRM with the student.
6. If they describe a completed degree (not eligible), inform them and direct to advisor.
7. Once scenario is confirmed, follow the matching question flow from the policy digest.
8. Ask the user which CPS courses the student wants credit for. When doing so, always include these two links:
   - ITC courses: https://catalog.northeastern.edu/course-descriptions/itc/
   - ALY courses: https://catalog.northeastern.edu/course-descriptions/aly/
   Tell the student: if their course is outside ITC/ALY, they should describe the subject area
   and select "Other" — an advisor will help identify the match.
9. Once all information is collected, produce:
   (a) A document checklist showing what they still need to gather
   (b) A brief evaluator-ready summary of their case
   Always put each piece of collected information on its own line with a blank line between them.
 
IMPORTANT: Each step = exactly one message from you. One step. One question. One send.

POLICY DIGEST:
{POLICY_DIGEST}
 
DATA TO COLLECT (JSON schema keys):
{json.dumps(INTERVIEW_SCHEMA, indent=2)}
""".strip()


# ===============================
# Azure OpenAI Client Factory
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
        return None, f"Client initialization failed: {type(e).__name__}"


# ===============================
# Static File Route (bulletproof)
# ===============================
@app.get("/static/<path:filename>")
def static_files(filename):
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    return send_from_directory(static_dir, filename)


# ===============================
# Basic Pages
# ===============================
@app.get("/")
def home():
    return render_template("index.html")


@app.get("/chat")
def chat_page():
    return render_template("chat.html")


@app.get("/admin")
def admin_page():
    status = {
        "AZURE_OPENAI_ENDPOINT": "✅ set" if os.getenv("AZURE_OPENAI_ENDPOINT") else "❌ missing",
        "AZURE_OPENAI_API_KEY": "✅ set" if os.getenv("AZURE_OPENAI_API_KEY") else "❌ missing",
        "AZURE_OPENAI_API_VERSION": os.getenv("AZURE_OPENAI_API_VERSION") or "(default: 2024-12-01-preview)",
        "AZURE_OPENAI_DEPLOYMENT": "✅ set" if os.getenv("AZURE_OPENAI_DEPLOYMENT") else "❌ missing",
        "SQL_CONNECTION_STRING": "✅ set" if os.getenv("SQL_CONNECTION_STRING") else "❌ missing",
    }
    return render_template("admin.html", status=status)


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


# ===============================
# DEBUG ROUTE — SDK versions
# ===============================
@app.get("/versions")
def versions():
    try:
        import openai
        import httpx
        return jsonify({
            "openai_version": getattr(openai, "__version__", "unknown"),
            "httpx_version": getattr(httpx, "__version__", "unknown"),
            "python_version": os.sys.version,
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ===============================
# DB CHECK ROUTE
# ===============================
@app.get("/dbcheck")
def dbcheck():
    conn_str = os.getenv("SQL_CONNECTION_STRING")
    if not conn_str:
        return jsonify({"error": "Missing SQL_CONNECTION_STRING"}), 500

    try:
        conn = pyodbc.connect(conn_str, timeout=10)
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        row = cursor.fetchone()
        conn.close()
        return jsonify({"status": "DB Connected", "result": int(row[0])})
    except Exception as e:
        app.logger.exception("DB connection check failed")
        return jsonify({
            "error": f"DB check failed: {type(e).__name__}",
            "details": str(e),
        }), 500


# ===============================
# DB Save Helper (safe — won't crash if DB not ready)
# Upserts by nuid: one row per student session, updated on every turn.
# Requires nuid to be a UNIQUE or PRIMARY KEY column in pla_sessions.
# ===============================
def save_session_to_db(nuid, student_name, scenario, conversation_log):
    conn_str = os.getenv("SQL_CONNECTION_STRING")
    if not conn_str:
        app.logger.warning("SQL_CONNECTION_STRING not set — skipping DB save.")
        return

    try:
        conn = pyodbc.connect(conn_str, timeout=10, autocommit=True)
        cursor = conn.cursor()
        conversation_text = json.dumps(conversation_log)[:4000]

        # Try to update an existing row first.
        # If no row exists yet (rowcount == 0), insert a new one.
        cursor.execute(
            """
            UPDATE pla_sessions
            SET student_name    = ?,
                scenario        = ?,
                conversation_log = ?,
                updated_at      = GETDATE()
            WHERE nuid = ?
            """,
            str(student_name),
            str(scenario),
            conversation_text,
            str(nuid),
        )

        if cursor.rowcount == 0:
            cursor.execute(
                """
                INSERT INTO pla_sessions (nuid, student_name, scenario, conversation_log)
                VALUES (?, ?, ?, ?)
                """,
                str(nuid),
                str(student_name),
                str(scenario),
                conversation_text,
            )
            app.logger.info(f"DB INSERT (new session) for NUID: {nuid}")
        else:
            app.logger.info(f"DB UPDATE (existing session) for NUID: {nuid}")

    except Exception as e:
        app.logger.exception(f"DB ERROR: {e}")


# ===============================
# Chat API Endpoint
# ===============================
@app.post("/api/chat")
def api_chat():
    try:
        data = request.get_json(silent=True) or {}
        user_message = (data.get("message") or "").strip()

        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
        if not deployment:
            return jsonify({"error": "Missing AZURE_OPENAI_DEPLOYMENT"}), 500

        client, err = get_client()
        if err:
            return jsonify({"error": err}), 500

        history = data.get("history") or []

        # Sanitise — only keep valid role/content pairs
        safe_history = [
            {"role": h["role"], "content": h["content"]}
            for h in history
            if isinstance(h, dict)
            and h.get("role") in ("user", "assistant")
            and isinstance(h.get("content"), str)
        ]

        response = client.chat.completions.create(
            model=deployment,
            messages=[
                {"role": "system", "content": build_system_prompt()},
            ] + safe_history + [
                {"role": "user", "content": user_message},
            ],
            temperature=0.3,
        )

        answer = (response.choices[0].message.content or "").strip()

        session_meta = data.get("session_meta") or {}
        nuid = session_meta.get("nuid")
        student_name = session_meta.get("student_name")
        scenario = session_meta.get("scenario")

        if nuid and student_name:
            full_history = safe_history + [
                {"role": "user", "content": user_message},
                {"role": "assistant", "content": answer},
            ]
            save_session_to_db(nuid, student_name, scenario, full_history)

        return jsonify({"answer": answer})

    except Exception as e:
        app.logger.exception("Azure OpenAI call failed")
        return jsonify({
            "error": f"Azure OpenAI call failed: {type(e).__name__}"
        }), 500


# ===============================
# Upload API Endpoint
# ===============================
ALLOWED_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg", ".docx"}
MAX_UPLOAD_BYTES = 10 * 1024 * 1024  # 10 MB

def _extract_text_from_upload(file_bytes: bytes, filename: str) -> tuple[str | None, str | None]:
    """
    Return (text_content, media_type) for the uploaded file.
    - PDF/images: return base64 + media_type for vision-capable model.
    - DOCX: extract plain text via python-docx (if available).
    - Fallback: try decoding as UTF-8 text.
    Returns (None, error_message) on failure.
    """
    ext = Path(filename).suffix.lower()

    if ext in (".png", ".jpg", ".jpeg"):
        media_type = "image/png" if ext == ".png" else "image/jpeg"
        b64 = base64.standard_b64encode(file_bytes).decode()
        return b64, media_type

    if ext == ".pdf":
        # Send as base64 PDF; GPT-4o vision can read PDFs directly
        b64 = base64.standard_b64encode(file_bytes).decode()
        return b64, "application/pdf"

    if ext == ".docx":
        try:
            import docx
            with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as tmp:
                tmp.write(file_bytes)
                tmp_path = tmp.name
            doc = docx.Document(tmp_path)
            os.unlink(tmp_path)
            text = "\n".join(p.text for p in doc.paragraphs if p.text.strip())
            return text, "text/plain"
        except ImportError:
            # python-docx not installed — fall through to UTF-8 attempt
            pass
        except Exception as e:
            return None, f"Could not read DOCX: {e}"

    # Generic: try UTF-8
    try:
        return file_bytes.decode("utf-8"), "text/plain"
    except Exception:
        return None, "Could not decode file as text."


@app.post("/api/upload")
def api_upload():
    try:
        # ── Validate file presence ──────────────────────────────────────────
        if "file" not in request.files:
            return jsonify({"error": "No file provided"}), 400

        uploaded = request.files["file"]
        filename = uploaded.filename or "upload"
        ext = Path(filename).suffix.lower()

        if ext not in ALLOWED_EXTENSIONS:
            return jsonify({"error": f"File type '{ext}' not supported. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"}), 400

        file_bytes = uploaded.read()
        if len(file_bytes) > MAX_UPLOAD_BYTES:
            return jsonify({"error": "File exceeds 10 MB limit."}), 400

        # ── Parse other form fields ─────────────────────────────────────────
        label = request.form.get("label", filename)
        history_raw = request.form.get("history", "[]")
        session_meta_raw = request.form.get("session_meta", "{}")

        try:
            history = json.loads(history_raw)
        except Exception:
            history = []

        try:
            session_meta = json.loads(session_meta_raw)
        except Exception:
            session_meta = {}

        # ── Azure OpenAI setup ──────────────────────────────────────────────
        deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
        if not deployment:
            return jsonify({"error": "Missing AZURE_OPENAI_DEPLOYMENT"}), 500

        client, err = get_client()
        if err:
            return jsonify({"error": err}), 500

        # ── Sanitise history ────────────────────────────────────────────────
        safe_history = [
            {"role": h["role"], "content": h["content"]}
            for h in history
            if isinstance(h, dict)
            and h.get("role") in ("user", "assistant")
            and isinstance(h.get("content"), str)
        ]

        # ── Build the user message that includes the file ───────────────────
        content_data, media_type = _extract_text_from_upload(file_bytes, filename)

        if content_data is None:
            # media_type holds the error string in this case
            return jsonify({"error": media_type}), 422

        if media_type == "text/plain":
            # Send as a text message
            user_content = [
                {
                    "type": "text",
                    "text": (
                        f"I have uploaded the document labeled '{label}' (filename: {filename}).\n\n"
                        f"Here is the extracted text content:\n\n{content_data}\n\n"
                        "Please acknowledge receipt, briefly summarise what you can see in this document "
                        "as it relates to my PLA request, note any gaps or issues, and then ask for the next document."
                    ),
                }
            ]
        elif media_type in ("image/png", "image/jpeg"):
            user_content = [
                {
                    "type": "text",
                    "text": (
                        f"I have uploaded the document labeled '{label}' (filename: {filename}). "
                        "Please acknowledge receipt, briefly summarise what you can see in this image "
                        "as it relates to my PLA request, note any gaps or issues, and then ask for the next document."
                    ),
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:{media_type};base64,{content_data}"},
                },
            ]
        else:
            # PDF as base64 — send as text with a note (vision models vary in PDF support)
            # Safer: extract first ~3000 chars of base64 as a text summary note
            user_content = [
                {
                    "type": "text",
                    "text": (
                        f"I have uploaded a PDF document labeled '{label}' (filename: {filename}). "
                        f"The file is {len(file_bytes) // 1024} KB. "
                        "Please acknowledge receipt of this PDF document, note it has been received for "
                        "the PLA review, and then ask for the next document."
                    ),
                }
            ]

        # ── Call the model ──────────────────────────────────────────────────
        response = client.chat.completions.create(
            model=deployment,
            messages=[
                {"role": "system", "content": build_system_prompt()},
            ] + safe_history + [
                {"role": "user", "content": user_content},
            ],
            temperature=0.3,
            max_tokens=800,
        )

        answer = (response.choices[0].message.content or "").strip()

        # ── Persist to DB if we have enough metadata ────────────────────────
        nuid = session_meta.get("nuid")
        student_name = session_meta.get("student_name")
        scenario = session_meta.get("scenario")

        if nuid and student_name:
            upload_note = f"[Uploaded '{label}': {filename}]"
            full_history = safe_history + [
                {"role": "user", "content": upload_note},
                {"role": "assistant", "content": answer},
            ]
            save_session_to_db(nuid, student_name, scenario, full_history)

        return jsonify({"answer": answer})

    except Exception as e:
        app.logger.exception("Upload handling failed")
        return jsonify({"error": f"Upload failed: {type(e).__name__}: {e}"}), 500


# ===============================
# Local Dev Entry Point
# ===============================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
