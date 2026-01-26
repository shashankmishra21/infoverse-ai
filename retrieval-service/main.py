from fastapi import FastAPI
from pydantic import BaseModel
from qdrant_client import QdrantClient
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

qdrant = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

COLLECTION_NAME = os.getenv("COLLECTION_NAME")
EMBED_API = os.getenv("EMBEDDING_API")


class QueryRequest(BaseModel):
    query: str


@app.post("/retrieve")
def retrieve_docs(req: QueryRequest):
    # Convert query → embedding
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


    # Format response
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