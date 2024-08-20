import openai
from llama_index.llms.openai import OpenAI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings

import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
Settings.llm = OpenAI(
        model="gpt-4o-mini",
        temperature=0,
        system_prompt="""You are an expert on the Streamlit Python library and your job is to answer technical questions. 
        Assume that all questions are related to the Streamlit Python library. Keep your answers technical and based on 
        facts – do not hallucinate features.""",
    )

class LlamaIndexAgent:
    def __init__(self, request):
        self.request = request

    def perceiver(self):
        content = SimpleDirectoryReader(input_dir=self.request, recursive=True)
        query = content.load_data()
        return query

    def actor(self):
        query = self.perceiver()
        index = VectorStoreIndex.from_documents(query)
        return index