"use client";

import { useState } from "react";
import { askQuestion } from "@/lib/api";

export default function AskPage() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState<any>(null);

  async function handleAsk() {
    const res = await askQuestion({
      question,
      context: { max_chunks: 5 },
    });
    setAnswer(res);
  }

  return (
    <div>
      <h1 className="text-xl font-semibold mb-4">Ask a Question</h1>

      <textarea
        className="w-full border p-2 mb-4"
        rows={4}
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button
        className="bg-black text-white px-4 py-2"
        onClick={handleAsk}
      >
        Ask
      </button>

      {answer && (
        <div className="mt-6">
          <h2 className="font-semibold">Answer</h2>
          <p className="mt-2">{answer.answer}</p>
        </div>
      )}
    </div>
  );
}
