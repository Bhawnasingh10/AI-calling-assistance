import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

def get_agent_response(query: str) -> str:
    try:
        payload = {
            "model": MODEL_NAME,
            "prompt": f"You are an AI call assistant. Respond to the user query: {query}",
            "stream": False
        }
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"Agent Error: {e}"
