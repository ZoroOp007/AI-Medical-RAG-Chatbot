from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

import os
#step 1: Load raw PDF 

DATA_PATH = "data/"

def upload_file_to_data( filename ):
    pass


def load_pdf_files(data):

    if data != "":
        os.makedirs(data , exist_ok=True)

    loader = DirectoryLoader(data,
                             glob="*.pdf",
                             loader_cls=PyPDFLoader
                             )

    documents = loader.load()
    return documents

documents=load_pdf_files(data=DATA_PATH)
print(f"Length of PDF pages : {len(documents)}")


#step 2: Create Chunks

def create_chunks(extracted_data):
    text_spillter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=50)

    text_chunks = text_spillter.split_documents(extracted_data)

    return text_chunks

text_chunks = create_chunks(extracted_data=documents)

#step 3: Create Vector Embeddings

def get_embedding_model():
    embedding_model = HuggingFaceEmbeddings(model_name = "Qwen/Qwen3-Embedding-0.6B")
    return embedding_model

embedding_model = get_embedding_model()

#step 4: Store embedding in FAISS

DB_FAISS_PATH = "vectorstore/db_faiss"
db = FAISS.from_documents(text_chunks , embedding_model)
db.save_local(DB_FAISS_PATH)

