from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

collection = os.getenv("COLLECTION_NAME")

info = client.get_collection(collection)

print("Collection Name:", collection)
print("Total Points (Chunks):", info.points_count)