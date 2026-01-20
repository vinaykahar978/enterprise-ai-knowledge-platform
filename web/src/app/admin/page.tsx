"use client";

import { useEffect, useState } from "react";

export default function AdminPage() {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/admin/memory")
      .then((res) => res.json())
      .then((res) => {
        setData(res);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  return (
    <div className="max-w-5xl mx-auto space-y-8">
      {/* Header */}
      <div>
        <h1 className="text-2xl font-semibold tracking-tight">
          Admin & Observability
        </h1>
        <p className="text-sm text-slate-500 mt-1">
          System state, memory, and AI observability (read-only)
        </p>
      </div>

      {/* Status Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="bg-slate-50 border border-slate-100 rounded-lg p-4">
          <div className="text-xs text-slate-500">System Status</div>
          <div className="text-sm font-medium text-green-700 mt-1">
            ● Online
          </div>
        </div>

        <div className="bg-slate-50 border border-slate-100 rounded-lg p-4">
          <div className="text-xs text-slate-500">Memory Mode</div>
          <div className="text-sm font-medium mt-1">
            Session + Verified
          </div>
        </div>

        <div className="bg-slate-50 border border-slate-100 rounded-lg p-4">
          <div className="text-xs text-slate-500">Access Level</div>
          <div className="text-sm font-medium mt-1">
            Read-only
          </div>
        </div>
      </div>

      {/* Memory Viewer */}
      <div className="bg-slate-50 border border-slate-100 rounded-lg p-6">
        <h2 className="text-lg font-semibold mb-2">
          Memory State
        </h2>
        <p className="text-sm text-slate-500 mb-4">
          Current in-memory state used by the AI system
        </p>

        {loading && (
          <div className="text-sm text-slate-500">
            Loading memory…
          </div>
        )}

        {!loading && data && (
          <pre
            className="
              bg-white
              border border-slate-100
              rounded-md
              p-4 text-xs
              overflow-auto
              max-h-[500px]
            "
          >
            {JSON.stringify(data, null, 2)}
          </pre>
        )}

        {!loading && !data && (
          <div className="text-sm text-red-600">
            Failed to load admin data
          </div>
        )}
      </div>
    </div>
  );
}
