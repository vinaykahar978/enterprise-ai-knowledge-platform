const API_BASE = "http://127.0.0.1:8000";

export async function askQuestion(payload: any) {
  const res = await fetch(`${API_BASE}/ask`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  return res.json();
}

export async function uploadDocument(file: File) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${API_BASE}/documents/upload`, {
    method: "POST",
    body: formData,
  });

  return res.json();
}
