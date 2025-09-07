
import os
from dotenv import load_dotenv

load_dotenv()
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.chains import retrieval_qa
from langchain_huggingface import HuggingFaceEmbeddings


#Step1 : setup llm (Mistral with HuggingFace)

HF_TOKEN = os.environ.get("HF_TOKEN")
huggingface_repo_id = "mistral/Mistral-7B-Instruct-v0.3"

def load_llm(huggingface_repo_id):
    llm = HuggingFaceEndpoint(
        repo_id = huggingface_repo_id,
        temperature = 0.5,
        model_kwargs= {
            "token":HF_TOKEN,
            "max_length" : "512"
        }
    )

#Step2 : Connect LLM with FAISS and Create Chain

custom_prompt_template = """
Use the piece of information provided in the context to answer user's question.
If you don't know, just say that you don't know, don't try to make up an answer.
Don't provide anything out of the given context

Context:{context}
Question:{question}

Start the answer directly. No small talk please.
"""

def set_custom_prompt(custom_prompt_template):
    prompt = PromptTemplate(template=custom_prompt_template , input_variables=["context" , "question"])
    return prompt

