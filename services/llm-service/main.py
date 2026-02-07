from fastapi import FastAPI
from pydantic import BaseModel
from llm import generate_answer
from prompt import build_prompt

app = FastAPI()


class GenerateRequest(BaseModel):
    question: str
    contexts: list[str]


@app.post("/generate")
def generate(req: GenerateRequest):
    prompt = build_prompt(req.contexts, req.question)

    answer = generate_answer(prompt)

    # HARD RAG GUARD
    if not answer or "not found in knowledge base" in answer.lower():
        answer = "Not found in knowledge base"

    return {"answer": answer}