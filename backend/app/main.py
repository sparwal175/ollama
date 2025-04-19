from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

OLLAMA_URL = "http://ollama:11434/api/generate"
GEMMA_URL = "http://gemma:8080/generate"

def call_ollama(prompt):
    payload = {
        "model": "llama2",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "Ollama failed.")

def call_gemma(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 100}
    }
    response = requests.post(GEMMA_URL, json=payload)
    try:
        return response.json()[0]["generated_text"]
    except Exception:
        return "Gemma failed."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_prompt = data.get("prompt", "Hello, Ollama and Gemma!")

    history = []
    speaker = "Ollama"
    message = user_prompt

    for i in range(4):  # 4-turn conversation
        if speaker == "Ollama":
            reply = call_ollama(message)
            history.append({"from": "Ollama", "message": reply})
            speaker = "Gemma"
            message = reply
        else:
            reply = call_gemma(message)
            history.append({"from": "Gemma", "message": reply})
            speaker = "Ollama"
            message = reply

    return jsonify(history)

@app.route("/")
def health():
    return "Ollama <-> Gemma Chat API running!"
