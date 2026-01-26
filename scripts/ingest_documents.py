import os
import uuid
import requests
from qdrant_client import QdrantClient
from dotenv import load_dotenv


load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "infoverse_documents")
EMBEDDING_API = os.getenv("EMBEDDING_API", "http://localhost:8001/embed")


if not QDRANT_URL or not QDRANT_API_KEY:
    raise ValueError("QDRANT_URL or QDRANT_API_KEY is missing")

# Init Qdrant client
client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

# Sample documents (demo only) (replace later with PDFs, DB, etc.)
documents = [
    "Infoverse AI is an enterprise RAG platform for intelligent knowledge management.",
    "It uses vector databases and retrieval augmented generation.",
    "Qdrant is used for high performance semantic search.",
    "MiniLM provides lightweight open-source embeddings."
]

def embed_text(text: str):
    response = requests.post(EMBEDDING_API, json={"text": text})

    if response.status_code != 200:
        raise RuntimeError("Embedding service failed")

    return response.json()["embedding"]

points = []

for doc in documents:
    embedding = embed_text(doc)

    points.append({
        "id": str(uuid.uuid4()),
        "vector": embedding,
        "payload": {
            "text": doc,
            "source": "manual_test"
        }
    })


client.upsert(
    collection_name=COLLECTION_NAME,
    points=points
)

print(f"Ingested {len(points)} documents into Qdrant")