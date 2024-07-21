import warnings
warnings.filterwarnings("ignore")

from pytest import mark
from app.agents.llamaparse import LlamaParseAgent as Agent
import nest_asyncio
nest_asyncio.apply()


@mark.asyncio
@mark.agent
@mark.llamaparse
class AgentTests:
    async def test_agent_behaviours(self):
        request = """app/data/business/invoice.jpeg"""
        agent_instance = Agent(request)
        result = await agent_instance.actor()
        print(result)
        assert result is not None