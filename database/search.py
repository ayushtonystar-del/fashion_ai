import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(
    path="./database/chroma_db"
)

collection = client.get_collection(
    "fashion_styles"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

query = "summer casual outfit"

query_embedding = model.encode(
    query
).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

print(results["documents"])