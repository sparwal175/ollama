import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

url = os.getenv("OLLAMA_URL")
headers = {"Content-Type": "application/json"}

# Get user input for first model and prompt
first_model = input("Enter the first model name (e.g., llama3, mistral): ")
prompt = input(f"[{first_model}] Enter your prompt: ")

# Helper function to process streamed response
def get_streamed_response(data):
    response_text = ""
    try:
        with requests.post(url, headers=headers, data=json.dumps(data), stream=True) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if line:
                    chunk = json.loads(line.decode('utf-8'))
                    response_text += chunk.get("response", "")
        return response_text
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None

# Step 1: Get output from the first model
first_data = {
    "model": first_model,
    "prompt": prompt
}

print(f"\n🔁 Getting response from [{first_model}]...")
first_output = get_streamed_response(first_data)
print(f"\n🔁 Output from [{first_model}]:\n{first_output}")

# Step 2: Pass output to the second model
if first_output:
    second_model = "gemma3:1b"
    second_data = {
        "model": second_model,
        "prompt": first_output
    }

    print(f"\n🎯 Sending to [{second_model}]...")
    second_output = get_streamed_response(second_data)
    print(f"\n🎯 Final Output from [{second_model}]:\n{second_output}")
