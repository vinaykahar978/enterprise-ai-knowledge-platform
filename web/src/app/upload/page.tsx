"use client";

import { useState } from "react";
import { uploadDocument } from "@/lib/api";

export default function UploadPage() {
  const [file, setFile] = useState<File | null>(null);
  const [status, setStatus] = useState<
    "idle" | "uploading" | "success" | "error"
  >("idle");
  const [message, setMessage] = useState<string>("");

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a file first");
      return;
    }

    setStatus("uploading");
    setMessage("Uploading document…");

    try {
      await uploadDocument(file);
      setStatus("success");
      setMessage("Document uploaded and indexed successfully");
      setFile(null);
    } catch {
      setStatus("error");
      setMessage("Upload failed. Please try again.");
    }
  };

  return (
    <div className="max-w-2xl mx-auto space-y-8">
      {/* Header */}
      <div>
        <h1 className="text-2xl font-semibold tracking-tight">
          Upload Documents
        </h1>
        <p className="text-sm text-slate-500 mt-1">
          Documents will be chunked, embedded, and indexed for retrieval
        </p>
      </div>

      {/* Upload Card */}
      <div className="bg-white border border-slate-200 rounded-lg p-6 space-y-6">
        {/* File Picker */}
        <label
          htmlFor="file-upload"
          className={`
            flex flex-col items-center justify-center
            border-2 border-dashed rounded-lg p-8
            cursor-pointer transition
            ${
              file
                ? "border-slate-400 bg-slate-50"
                : "border-slate-300 hover:border-slate-500"
            }
          `}
        >
          <input
            id="file-upload"
            type="file"
            className="hidden"
            onChange={(e) => {
              const selected = e.target.files?.[0];
              setFile(selected || null);
              setStatus("idle");
              setMessage("");
            }}
          />

          {!file ? (
            <>
              <div className="text-sm font-medium text-slate-700">
                Click to select a document
              </div>
              <div className="text-xs text-slate-500 mt-1">
                PDF or TXT files supported
              </div>
            </>
          ) : (
            <>
              <div className="text-sm font-medium text-slate-800">
                Selected file
              </div>
              <div className="text-xs text-slate-600 mt-1">
                {file.name}
              </div>
            </>
          )}
        </label>

        {/* Action Row */}
        <div className="flex items-center justify-between">
          <div className="text-sm text-slate-500">
            Files are processed asynchronously
          </div>

          <button
            onClick={handleUpload}
            disabled={!file || status === "uploading"}
            className={`
              px-5 py-2 text-sm font-medium rounded-md transition
              ${
                status === "uploading"
                  ? "bg-slate-400 text-white cursor-not-allowed"
                  : file
                  ? "bg-slate-900 text-white hover:bg-slate-800"
                  : "bg-slate-200 text-slate-500 cursor-not-allowed"
              }
            `}
          >
            {status === "uploading" ? "Uploading…" : "Upload"}
          </button>
        </div>
      </div>

      {/* Status Message */}
      {message && (
        <div
          className={`
            text-sm rounded-md p-3 border
            ${
              status === "success"
                ? "bg-green-50 text-green-700 border-green-200"
                : status === "error"
                ? "bg-red-50 text-red-700 border-red-200"
                : "bg-slate-50 text-slate-700 border-slate-200"
            }
          `}
        >
          {message}
        </div>
      )}
    </div>
  );
}
