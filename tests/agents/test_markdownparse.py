import warnings
warnings.filterwarnings("ignore")

from pytest import mark
from app.agents.markdownparse import MarkdownParseAgent as Agent
import pprint
import nest_asyncio
nest_asyncio.apply()
import time


@mark.asyncio
@mark.agent
@mark.markdownparse
class AgentTests:
    async def test_agent_behaviours(self):
        request = """app/data/business/invoice.pdf"""
        begin = time.time()
        agent_instance = Agent(request)
        result = await agent_instance.actor()
        end = time.time()
        pprint.pprint(result)
        print(f"Time taken: {end - begin}")
        assert result is not None