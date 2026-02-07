import requests

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"
MODEL = "phi3:mini"

def clean_output(text: str):
    if not text:
        return ""

    # Remove prompt leakage if model repeats instructions
    if "Answer:" in text:
        text = text.split("Answer:")[-1]

    if "Final Answer:" in text:
        text = text.split("Final Answer:")[-1]

    return text.strip()


def generate_answer(prompt: str):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "temperature": 0,
        "top_p": 0.1
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    data = response.json()
    raw_output = data.get("response", "")

    return clean_output(raw_output)