from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document
import os

def load_pdf_file(data):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR, data)

    loader = DirectoryLoader(DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)

    documents = loader.load()
    return documents


def filter_short_documents(documents: List[Document]) -> List[Document]:
    filtered_documents = []
    for doc in documents:
        src = doc.metadata.get("source")
        filtered_documents.append(
            Document(page_content=doc.page_content, metadata={"source": src})
        )
    return filtered_documents


# ✅ EXACT SAME AS YOUR FUNCTION
def text_spliting(filtered_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    docs = text_splitter.split_documents(filtered_docs)
    return docs
