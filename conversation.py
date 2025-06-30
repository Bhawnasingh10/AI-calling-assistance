import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

def summarize_conversation(transcript: str) -> str:
    try:
        prompt = (
            f"Summarize the following conversation between a user and an AI assistant:\n\n{transcript}\n\n"
            "Give a brief summary:"
        )
        response = requests.post(OLLAMA_URL, json={"model": MODEL_NAME, "prompt": prompt, "stream": False})
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"Summary Error: {e}"
