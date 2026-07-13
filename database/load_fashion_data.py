import json
import chromadb

from sentence_transformers import (
    SentenceTransformer
)

client = chromadb.PersistentClient(
    path="./database/chroma_db"
)

collection = client.get_or_create_collection(
    name="fashion_styles"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

with open(
    "metadata/fashion_knowledge.json",
    "r"
) as f:

    data = json.load(f)

for item in data:

    embedding = model.encode(
        item["description"]
    ).tolist()

    collection.add(

        ids=[item["id"]],

        documents=[
            item["description"]
        ],

        embeddings=[embedding]
    )

print("Data Loaded")