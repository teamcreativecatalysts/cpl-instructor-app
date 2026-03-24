let currentNUID = null;

document.getElementById("send").addEventListener("click", async () => {
  const msg = document.getElementById("msg").value.trim();
  const out = document.getElementById("out");

  if (/^\d{9}$/.test(msg)) {
    currentNUID = msg;
  }

  if (!msg) {
    out.textContent = "Please type a message first.";
    return;
  }

  out.textContent = "Thinking...";

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg }),
    });

    const text = await res.text();
    let data = null;
    try { data = JSON.parse(text); } catch (_) {}

    if (!res.ok) {
      out.textContent = data?.error
        ? `Error (${res.status}): ${data.error}`
        : `Error (${res.status}): ${text}`;
      return;
    }

    out.textContent = data?.answer ?? text;

  } catch (e) {
    out.textContent = `Network error: ${e}`;
  }
});


// ==============================
// Upload function (ADDED)
// ==============================
async function uploadFile(docType) {
  const fileInput = document.querySelector('input[type="file"]');
  const file = fileInput?.files?.[0];

  if (!file) {
    alert("Please select a file");
    return;
  }

  if (!currentNUID) {
    alert("Please enter your NUID first in the chat.");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);
  formData.append("nuid", currentNUID);
  formData.append("document_type", docType);

  try {
    await fetch("/api/upload", {
      method: "POST",
      body: formData
    });

    const out = document.getElementById("out");

    // Show upload confirmation
    out.textContent = `Uploaded ${docType} successfully. Continuing...`;

    // Continue chatbot flow
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: "UPLOAD_COMPLETE" })
    });

    const text = await res.text();
    let data = null;
    try { data = JSON.parse(text); } catch (_) {}

    out.textContent = data?.answer ?? text;

  } catch (e) {
    document.getElementById("out").textContent = `Upload failed: ${e}`;
  }
}

