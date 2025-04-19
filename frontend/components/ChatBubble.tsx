type ChatBubbleProps = {
    from: string;
    message: string;
  };
  
  export default function ChatBubble({ from, message }: ChatBubbleProps) {
    const isOllama = from === "Ollama";
    return (
      <div className={`flex ${isOllama ? 'justify-start' : 'justify-end'} my-2`}>
        <div className={`rounded-2xl p-3 max-w-xl shadow-md ${isOllama ? 'bg-gray-200 text-black' : 'bg-blue-600 text-white'}`}>
          <strong>{from}:</strong> {message}
        </div>
      </div>
    );
  }
  