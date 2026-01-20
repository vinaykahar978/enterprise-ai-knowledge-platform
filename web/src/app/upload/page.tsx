"use client";

import { useState } from "react";
import { uploadDocument } from "@/lib/api";

export default function UploadPage() {
  const [file, setFile] = useState<File | null>(null);
  const [status, setStatus] = useState("");

  async function handleUpload() {
    if (!file) return;
    await uploadDocument(file);
    setStatus("Uploaded successfully");
  }

  return (
    <div>
      <h1 className="text-xl font-semibold mb-4">Upload Document</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
      />

      <button
        className="ml-4 bg-black text-white px-4 py-2"
        onClick={handleUpload}
      >
        Upload
      </button>

      {status && <p className="mt-4">{status}</p>}
    </div>
  );
}
