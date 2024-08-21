import os
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage
)
from llama_index.core.agent.react import ReActAgent
from llama_index.core.workflow import (
    step,
    Context,
    Workflow,
    Event,
    StartEvent,
    StopEvent
)
from llama_index.llms.openai import OpenAI
from llama_index.core.postprocessor.rankGPT_rerank import RankGPTRerank
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.chat_engine import SimpleChatEngine
from llama_index.utils.workflow import draw_all_possible_flows

import openai
import os
from dotenv import load_dotenv
load_dotenv()

class JudgeEvent(Event):
    query: str

class BadQueryEvent(Event):
    query: str

class NaiveRAGEvent(Event):
    query: str

class HighTopKEvent(Event):
    query: str

class RerankEvent(Event):
    query: str

class ResponseEvent(Event):
    query: str
    response: str

class SummarizeEvent(Event):
    query: str
    response: str

class LlamaIndexWorkflow(Workflow):
    def __init__(self, data_dir, persist_dir):
        self.data_dir = data_dir
        self.persist_dir = persist_dir

    def actor(self):
        if os.path.exists(self.persist_dir):
            print("Loading existing index...")
            storage_context = StorageContext.from_defaults(persist_dir=self.persist_dir)
            index = load_index_from_storage(storage_context)
        else:
            print("Creating new index...")
            documents = SimpleDirectoryReader(self.data_dir).load_data()
            index = VectorStoreIndex.from_documents(documents)
            index.storage_context.persist(persist_dir=self.persist_dir)

        return index