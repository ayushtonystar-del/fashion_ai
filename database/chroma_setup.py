import chromadb

client = chromadb.PersistentClient(
    path="./database/chroma_db"
)

collection = client.get_or_create_collection(
    name="fashion_styles"
)

print("ChromaDB Ready")