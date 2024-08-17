import warnings
warnings.filterwarnings("ignore")

from pytest import mark
from app.agents.llamaparse import LlamaParseAgent as Agent
import nest_asyncio
nest_asyncio.apply()
import time


@mark.agent
@mark.llamaparse
class AgentTests:
    def test_agent_behaviours(self):
        request = """app/data/business/invoice.pdf"""
        begin = time.time()
        agent_instance = Agent(request)
        response = agent_instance.actor()
        end = time.time()
        print(response)
        print(f"Time taken: {end - begin}")
        assert response is not None