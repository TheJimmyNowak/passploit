from sentence_transformers import SentenceTransformer
from chromadb.config import Settings
from chromadb import PersistentClient
from chromadb.utils import embedding_functions
import os
import numpy as np
from tqdm import tqdm  # For progress tracking

def store_passwords(passwords, batch_size=100):
    """
    Stores embeddings of passwords into ChromaDB vector store in batches.
    :param passwords: List of passwords.
    :param batch_size: Number of passwords to process in one batch.
    """
    # Prepare batches
    for i in tqdm(range(0, len(passwords), batch_size), desc="Processing batches"):
        batch = passwords[i:i + batch_size]
        
        # Generate embeddings for the batch
        embeddings = model.encode(batch, batch_size=batch_size, convert_to_numpy=True)
        
        # Prepare data for the vector store
        ids = [str(i + j) for j in range(len(batch))]
        collection.add(ids=ids, documents=batch, embeddings=embeddings.tolist())
    
    print(f"All {len(passwords)} passwords added to vector store successfully.")


def main():
    # Initialize SentenceTransformer model
    model_name = "all-MiniLM-L6-v2"
    model = SentenceTransformer(model_name, device="cuda")
    
    db_directory = "./chroma_db"
    client = PersistentClient(path=db_directory)
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)
    
    collection_name = "password_embeddings"
    collection = client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_fn
    )


if __name__ == "__main__":
    import os

    # Check if the vector store directory exists
    if not os.path.exists("./chroma_vector_store"):
        print("First-time setup: Adding common passwords to vector store.")
        passwords = load_all_passwords()
        store_passwords(passwords)