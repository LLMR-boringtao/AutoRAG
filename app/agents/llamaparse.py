from pathlib import Path
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader
from app.plugins.EnsureLocalFile import EnsureLocalFile

import os
from dotenv import load_dotenv
load_dotenv()


class LlamaParseAgent:
    def __init__(self, request):
        self.request = request
        self.parser = LlamaParse(
            result_type="markdown",
            invalidate_cache=True,
            do_not_cache=True,
            num_workers=9,
            language="ch_sim",
            use_vendor_multimodal_model=True,
            vendor_multimodal_model_name="openai-gpt-4o-mini",
            # vendor_multimodal_api_key=os.getenv("OPENAI_API_KEY"),
            parsing_instruction = "读取文件中表格的结构与内容，忽略表格以外的内容。"
        )

    async def actor(self):
        file_name = EnsureLocalFile(str(self.request))
        file_content = self.parser.load_data(file_name)
        result = file_content[0].text
    
        return result