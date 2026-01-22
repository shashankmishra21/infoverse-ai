from fastapi import FastAPI;
from pydantic import BaseModel;
from sentence_transformers import SentenceTransformer;

model = SentenceTransformer('all-MiniLM-L6-v2')

app = FastAPI(title="Infoverse Embedding Service", version="1.0.0")

class EmbedRequest(BaseModel):
    text: str

class EmbedResponse(BaseModel):
    embedding: list[float]
    dimension: int

@app.get("/health")
def health():
    return {"status": "ok"}
    
@app.post("/embed", response_model=EmbedResponse)
def embed(req: EmbedRequest):
    if not req.text.strip():
        return {
            "embedding": [],
            "dimension": 0
        }
    vector = model.encode(req.text).tolist()
    return {
        "embedding": vector,
        "dimension": len(vector)
    }

