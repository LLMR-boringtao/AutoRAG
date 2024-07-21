from http import HTTPStatus
import dashscope
from app.plugins.ensure_local_file import ensure_local_file


class QwenVLAgent:
    def __init__(self, request):
        self.request = request
        
    async def actor(self):
        file_name = ensure_local_file(str(self.request))
        messages = [
            {
                "role": "user",
                "content": [
                    {"image": file_name},
                    {"text": "读取文件中表格的结构"}
                ]
            }
        ]
        response = dashscope.MultiModalConversation.call(model='qwen-vl-max', messages=messages)
        result = response["output"]["choices"][0]["message"]["content"][0]["text"]
    
        return result