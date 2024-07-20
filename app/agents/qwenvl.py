from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
from app.plugins.ensure_local_file import ensure_local_file

import torch
torch.manual_seed(1234)


class QwenVLAgent:
    def __init__(self, request):
        self.request = request
        self.tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-VL", trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-VL", device_map="cpu", trust_remote_code=True).eval()
        self.model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-VL", trust_remote_code=True)

    async def actor(self):
        file_name = ensure_local_file(str(self.request))
        query = self.tokenizer.from_list_format([
            {'image': file_name}, 
            {'text': '读取文件中表格的结构'},
        ])
        inputs = self.tokenizer(query, return_tensors='pt')
        inputs = inputs.to(self.model.device)
        pred = self.model.generate(**inputs)
        response = self.tokenizer.decode(pred.cpu()[0], skip_special_tokens=False)
        result = response
    
        return result