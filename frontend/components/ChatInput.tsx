"use client";

import { useState } from "react";

export default function ChatInput({ onSend }: { onSend: (message: string) => void }) {
  const [text, setText] = useState("");

  const sendMessage = () => {
    if (!text.trim()) return;
    onSend(text);
    setText("");
  };

  return (
    <div className="flex gap-2 p-4 border-t">
      <input
        className="flex-1 rounded-xl border px-4 py-2"
        placeholder="Type your message..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && sendMessage()}
      />
      <button className="bg-blue-600 text-white px-4 py-2 rounded-xl" onClick={sendMessage}>
        Send
      </button>
    </div>
  );
}
