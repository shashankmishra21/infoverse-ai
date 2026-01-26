from fastapi import FastAPI
from pydantic import BaseModel
from qdrant_client import QdrantClient
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Infoverse Retrieval Service")

# Config
qdrant = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

COLLECTION_NAME = os.getenv("COLLECTION_NAME")
EMBED_API = os.getenv("EMBEDDING_API")

# LLM Service URL
LLM_API = "http://127.0.0.1:8003"

class QueryRequest(BaseModel):
    query: str

# Retrieve Chunks Endpoint

@app.post("/retrieve")
def retrieve_docs(req: QueryRequest):

    # Convert query to embedding
    embed_res = requests.post(
        f"{EMBED_API}/embed",
        json={"text": req.query}
    )

    vector = embed_res.json()["embedding"]

    # Search Qdrant
    results = qdrant.query_points(
        collection_name=COLLECTION_NAME,
        query=vector,
        limit=5,
        with_payload=True
    ).points

    hits = []
    for r in results:
        hits.append({
            "score": r.score,
            "text": r.payload["text"],
            "metadata": r.payload.get("metadata", {})
        })

    return {
        "query": req.query,
        "results": hits
    }

# FULL RAG Endpoint (/ask)

@app.post("/ask")
def ask(req: QueryRequest):

    # Step 1: Retrieve relevant chunks
    retrieved = retrieve_docs(req)
    chunks = [hit["text"] for hit in retrieved["results"]]

    # Step 2: Send chunks to LLM service
    llm_res = requests.post(
        f"{LLM_API}/generate",
        json={
            "question": req.query,
            "contexts": chunks
        }
    )

    answer = llm_res.json()["answer"]

    return {
        "query": req.query,
        "answer": answer,
        "sources": retrieved["results"]
    }