import warnings
warnings.filterwarnings("ignore")

from pytest import mark
from app.agents.qwenvl import QwenVLAgent as Agent
import time


@mark.asyncio
@mark.agent
@mark.qwenvl
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