"use client";

import { useState } from "react";
import { askQuestion } from "@/lib/api";

export default function AskPage() {
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);
  const [answer, setAnswer] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  async function handleAsk() {
    if (!question.trim()) return;

    setLoading(true);
    setError(null);
    setAnswer(null);

    try {
      const res = await askQuestion({ question });
      setAnswer(res);
    } catch (e) {
      setError("Failed to get answer");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="max-w-3xl mx-auto space-y-8">
      {/* Header */}
      <div>
        <h1 className="text-2xl font-semibold tracking-tight">
          Ask the Knowledge Base
        </h1>
        <p className="text-sm text-slate-500 mt-1">
          Answers are grounded in internal documents
        </p>
      </div>

      {/* Question Input */}
      <div className="bg-white border border-slate-200 rounded-lg p-4 space-y-4">
        <textarea
          className="w-full resize-none rounded-md border border-slate-300 p-3 text-sm focus:outline-none focus:ring-2 focus:ring-slate-400"
          rows={4}
          placeholder="Ask a question about internal documents..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <div className="flex justify-end">
          <button
            onClick={handleAsk}
            disabled={loading}
            className="px-5 py-2 text-sm font-medium rounded-md bg-slate-900 text-white hover:bg-slate-800 disabled:opacity-50 transition"
          >
            {loading ? "Thinking…" : "Ask"}
          </button>
        </div>
      </div>

      {/* Error */}
      {error && (
        <div className="text-sm text-red-600 bg-red-50 border border-red-200 rounded-md p-3">
          {error}
        </div>
      )}

      {/* Answer */}
      {answer?.answer && (
        <div className="bg-white border border-slate-200 rounded-lg p-6 space-y-4">
          <h2 className="text-sm font-semibold text-slate-600 uppercase">
            Answer
          </h2>
          <p className="text-slate-900 leading-relaxed">
            {answer.answer}
          </p>
        </div>
      )}

      {/* Sources */}
      {answer?.sources && answer.sources.length > 0 && (
        <div className="bg-white border border-slate-200 rounded-lg p-6 space-y-4">
          <h3 className="text-sm font-semibold text-slate-600 uppercase">
            Sources
          </h3>

          <ul className="space-y-3">
            {answer.sources.map((s: any) => (
              <li
                key={s.chunk_id}
                className="border border-slate-200 rounded-md p-3 text-sm"
              >
                <div className="text-xs text-slate-500 mb-1">
                  Relevance score: {s.score.toFixed(2)}
                </div>
                <div className="text-slate-800 leading-snug">
                  {s.text}
                </div>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
