"use client";

import { useEffect, useState } from "react";

export default function AdminPage() {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/admin/memory")
      .then((res) => res.json())
      .then(setData);
  }, []);

  return (
    <div>
      <h1 className="text-xl font-semibold mb-4">Admin & Observability</h1>

      {!data && <p>Loading...</p>}

      {data && (
        <pre className="bg-gray-100 p-4 text-xs overflow-auto">
          {JSON.stringify(data, null, 2)}
        </pre>
      )}
    </div>
  );
}
