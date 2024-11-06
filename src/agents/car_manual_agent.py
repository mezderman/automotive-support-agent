import os
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    Settings,
)

import chromadb
from src.utils import load_prompt_template
from llama_index.vector_stores.chroma import ChromaVectorStore
from src.events.retrieval_event import RetrieveEvent


class CarManualAgent:
    def __init__(self, manual_dir):
        self.manual_dir = manual_dir
        self.index = None
        
        self._initialize_index()
        # global
        Settings.embed_model = HuggingFaceEmbedding(
            model_name="BAAI/bge-small-en-v1.5"
        )    

    def _initialize_index(self):
        collection_name = "cars_manuals"
        db = chromadb.PersistentClient(path="./chroma_db")

        existing_collections = db.list_collections()

        print(db.list_collections())

        # Check if the desired collection exists
        if collection_name in [collection.name for collection in existing_collections]:
            print("-- load vectors")
            chroma_collection = db.get_or_create_collection(collection_name)
            vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
            self.index = VectorStoreIndex.from_vector_store(
            vector_store,
        )
        else:
            # set up ChromaVectorStore and load in data
            print("-- create vectors")
            chroma_collection = db.get_or_create_collection(collection_name)
            vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
            storage_context = StorageContext.from_defaults(vector_store=vector_store)
             # Load documents from the specified directory
            reader = SimpleDirectoryReader(input_dir=self.manual_dir)
            documents = reader.load_data()
            self.index = VectorStoreIndex.from_documents(
                documents, storage_context=storage_context
            )

        
        # Create a query engine from the index
        self.query_engine = self.index.as_query_engine()
        self.retriever = self.index.as_retriever()


        
        

    def search_manual(self, query):
        # Load and format the prompt template with the query
        nodes = self.retriever.retrieve(query)
       
        # print(nodes)
        return nodes
