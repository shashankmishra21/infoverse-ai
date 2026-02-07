from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()


class QueryRequest(BaseModel):
    query: str


# ---------- PROMPT BUILDER (STRICT RAG) ----------
def build_prompt(context_chunks, question):
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a strict AI assistant.

You MUST answer ONLY from the given context.
Do NOT use outside knowledge.
Do NOT guess.
If the answer is not present in context, reply EXACTLY:
"Not found in knowledge base".

Context:
{context}

Question:
{question}

Answer:
"""
    return prompt


# ---------- RETRIEVAL ----------
def retrieve_docs(req: QueryRequest):
    embed_res = requests.post(
        "http://embedding-service:8001/embed",
        json={"text": req.query}
    )

    query_vector = embed_res.json()["embedding"]

    # Dummy retrieval (later Qdrant use hoga)
    return {
        "query": req.query,
        "results": [
            {"score": 0.9, "text": "RAG retrieves documents before answering."},
            {"score": 0.8, "text": "Embeddings help semantic search."}
        ]
    }

@app.post("/ask")
def ask(req: QueryRequest):
    retrieved = retrieve_docs(req)

    contexts = [r["text"] for r in retrieved["results"]]

    llm_res = requests.post(
        "http://llm-service:8003/generate",
        json={
            "question": req.query,
            "contexts": contexts
        }
    )

    llm_json = llm_res.json()

    answer = llm_json.get("answer") or llm_json.get("response")

    return {
        "query": req.query,
        "answer": answer,
        "contexts": contexts
    }