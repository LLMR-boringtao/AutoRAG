import warnings
warnings.filterwarnings("ignore")

from pytest import mark
from app.agents.llamaparse import LlamaParseAgent as Agent
import nest_asyncio
nest_asyncio.apply()
import time


@mark.asyncio
@mark.agent
@mark.llamaparse
class AgentTests:
    async def test_agent_behaviours(self):
        request = """app/data/business/invoice.jpeg"""
        begin = time.time()
        agent_instance = Agent(request)
        result = await agent_instance.actor()
        end = time.time()
        print(result)
        print(f"Time taken: {end - begin}")
        assert result is not None