import warnings
warnings.filterwarnings("ignore")

from pytest import mark
from app.agents.qwenvl_api import QwenVLAgent as Agent


@mark.asyncio
@mark.agent
@mark.qwenvl_api
class AgentTests:
    async def test_agent_behaviours(self):
        request = """app/data/business/invoice.jpeg"""
        agent_instance = Agent(request)
        result = await agent_instance.actor()
        print(result)
        assert result is not None