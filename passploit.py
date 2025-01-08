from sentence_transformers import SentenceTransformer
from chromadb.config import Settings
from chromadb import PersistentClient
from chromadb.utils import embedding_functions
import os
import numpy as np


class Passploit():
    def __init__(self):
        # Initialize SentenceTransformer model
        model_name = "all-MiniLM-L6-v2"
        self.model = SentenceTransformer(model_name, device="cuda")
        
        db_directory = "./chroma_db"
        self.client = PersistentClient(path=db_directory)
        embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)
        
        collection_name = "password_embeddings"
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=embedding_fn
        )
       
    
    
    def find_similar_passwords(self, target_data, n_results):
        """
        Finds and sorts passwords in similarity order to the target data.
        :param target_data: List of strings containing personal data.
        :return: List of sorted passwords by similarity.
        """
        # Generate embeddings for the target data
        target_embeddings = self.model.encode(target_data).tolist()
        # Query vector store
        query_results = self.collection.query(query_embeddings=target_embeddings, n_results=n_results)
    
        # Combine results and sort
        all_results = zip(query_results["documents"], query_results["distances"])
        
        sorted_results = sorted(all_results, key=lambda x: x[1])  # Lower distance is more similar
        return [doc for doc, _ in sorted_results]