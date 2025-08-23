from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

import os
#step 1. Load raw PDF 

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

# documents=load_pdf_files(data=DATA_PATH)
# print(f"Length of PDF pages : {len(documents)}")


#step 2. Create Chunks

def create_chunks(extracted_data):
    text_spillter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=50)

    text
