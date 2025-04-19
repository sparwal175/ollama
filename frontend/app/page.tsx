"use client";

import { useState } from "react";
import ChatBubble from "@/components/ChatBubble";
import ChatInput from "@/components/ChatInput";

type ChatResponse = { from: string; message: string }[];

export default function Home() {
  const [history, setHistory] = useState<ChatResponse>([]);
  const [loading, setLoading] = useState(false);

  const handleSend = async (userPrompt: string) => {
    setHistory([{ from: "User", message: userPrompt }]);
    setLoading(true);
    try {
      const res = await fetch("http://llm-chat-api:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: userPrompt }),
      });
      const data = await res.json();
      setHistory([{ from: "User", message: userPrompt }, ...data]);
    } catch (err) {
      setHistory([{ from: "User", message: userPrompt }, { from: "System", message: "Failed to fetch chat." }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gray-50 flex flex-col">
      <h1 className="text-center text-2xl font-bold my-6">Ollama ↔ Gemma Chat</h1>
      <div className="flex-1 px-4 overflow-auto">
        {history.map((entry, idx) => (
          <ChatBubble key={idx} from={entry.from} message={entry.message} />
        ))}
        {loading && <ChatBubble from="System" message="Thinking..." />}
      </div>
      <ChatInput onSend={handleSend} />
    </main>
  );
}
