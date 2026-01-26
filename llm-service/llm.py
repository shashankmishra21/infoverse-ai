import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral:latest"


def generate_answer(prompt: str):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["response"]