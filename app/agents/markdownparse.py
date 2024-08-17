
from app.plugins.EnsureLocalFile import EnsureLocalFile
from app.plugins.MarkdownElementNodeParser import MarkdownElementNodeParser
from app.agents.llamaparse import LlamaParseAgent
from llama_parse import LlamaParse

import os
from dotenv import load_dotenv
load_dotenv()


class MarkdownParseAgent:
    def __init__(self, request):
        self.request = request
        self.llamaparser = LlamaParse(
            result_type="markdown",
            language="ch_sim",
            use_vendor_multimodal_model=True,
            vendor_multimodal_model_name="openai-gpt-4o-mini",
            vendor_multimodal_api_key=os.getenv("OPENAI_API_KEY"),
            parsing_instruction = "读取文件中表格的结构与内容，忽略表格以外的内容。"
        )

    async def actor(self):
        file_name = EnsureLocalFile(str(self.request))
        documents = self.llamaparser.load_data(file_name)
        node_parser = MarkdownElementNodeParser(llm=None, num_workers=8)
        nodes = node_parser.get_nodes_from_documents(documents)
        base_nodes, node_mappings = node_parser.get_base_nodes_and_mappings(nodes)

        return node_mappings