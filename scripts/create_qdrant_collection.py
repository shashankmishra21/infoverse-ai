import os
from qdrant_client import QdrantClient
from dotenv import load_dotenv

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "infoverse_documents")

VECTOR_SIZE = 384
DISTANCE = "Cosine"

if not QDRANT_URL or not QDRANT_API_KEY:
    raise ValueError("QDRANT_URL or QDRANT_API_KEY is missing")

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)


client.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config={
        "size": VECTOR_SIZE,
        "distance": DISTANCE
    }
)



print("Qdrant collection recreated safely")
print(f"Vector size: {VECTOR_SIZE}")
print(f"Collection name: {COLLECTION_NAME}")