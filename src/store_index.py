import torch
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_pinecone import PineconeVectorStore


def download_embeddings():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={"device": "cuda" if torch.cuda.is_available() else "cpu"}
    )
    return embeddings


def store_index(text_chunks, embedding, index_name):

    # ✅ ONLY FIX: documents= instead of text_chunks=
    docstore = PineconeVectorStore.from_documents(
        documents=text_chunks,
        embedding=embedding,
        index_name=index_name
    )

    return docstore
