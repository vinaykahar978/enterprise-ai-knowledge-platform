"use client";

import { useState } from "react";
import { uploadDocument } from "@/lib/api";

export default function UploadPage() {
  const [file, setFile] = useState<File | null>(null);
  const [status, setStatus] = useState("");

  const handleUpload = async () => {
    if (!file) {
      setStatus("Please select a file first");
      return;
    }

    setStatus("Uploading...");

    try {
      await uploadDocument(file);
      setStatus("Upload successful");
    } catch {
      setStatus("Upload failed");
    }
  };

  return (
    <div className="max-w-xl">
      <h1 className="text-xl font-semibold mb-6">Upload Documents</h1>

      {/* FILE PICKER */}
      <label
        htmlFor="file-upload"
        className="flex flex-col items-center justify-center
                   border-2 border-dashed border-gray-300
                   rounded-lg p-6 cursor-pointer
                   hover:border-black transition"
      >
        <input
          id="file-upload"
          type="file"
          className="hidden"
          onChange={(e) => {
            const selectedFile = e.target.files?.[0];
            setFile(selectedFile || null);
          }}
        />

        {!file ? (
          <>
            <p className="text-sm text-gray-600">Click to choose a file</p>
            <p className="text-xs text-gray-400 mt-1">
              PDF, TXT supported
            </p>
          </>
        ) : (
          <>
            <p className="text-sm font-medium">Selected file:</p>
            <p className="text-xs text-gray-600 mt-1">{file.name}</p>
          </>
        )}
      </label>

      {/* UPLOAD BUTTON */}
      <button
        onClick={handleUpload}
        disabled={!file}
        className={`mt-4 px-4 py-2 rounded
          ${file ? "bg-black text-white" : "bg-gray-300 text-gray-600 cursor-not-allowed"}
        `}
      >
        Upload
      </button>

      {status && <p className="mt-4 text-sm">{status}</p>}
    </div>
  );
}
