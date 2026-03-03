from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

app = FastAPI()

# Load data
df = pd.read_csv("shl_catalog.csv")
index = faiss.read_index("faiss_index.index")
model = SentenceTransformer("all-MiniLM-L6-v2")

class QueryRequest(BaseModel):
    query: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recommend")
def recommend(request: QueryRequest):
    query_embedding = model.encode([request.query])
    D, I = index.search(np.array(query_embedding), 10)

    results = []
    for idx in I[0]:
        results.append({
            "assessment_name": df.iloc[idx]["name"],
            "url": df.iloc[idx]["url"]
        })

    return results
