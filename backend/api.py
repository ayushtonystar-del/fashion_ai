from fastapi import FastAPI
import chromadb

from sentence_transformers import (
    SentenceTransformer
)

app = FastAPI()

client = chromadb.PersistentClient(
    path="./database/chroma_db"
)

collection = client.get_collection(
    "fashion_styles"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

@app.get("/")
def home():

    return {
        "message":"Fashion AI Backend Running"
    }

@app.get("/recommend")
def recommend(query:str):

    embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    return {

        "query": query,

        "recommendations":
        results["documents"][0]
    }