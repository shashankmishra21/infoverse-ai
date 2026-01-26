from fastapi import FastAPI
from pydantic import BaseModel

from llm import generate_answer
from prompt import build_prompt

app = FastAPI(title="Infoverse LLM Service")


class GenerateRequest(BaseModel):
    question: str
    contexts: list[str]


@app.post("/generate")
def generate(req: GenerateRequest):
    prompt = build_prompt(req.contexts, req.question)
    answer = generate_answer(prompt)
    return {"answer": answer}