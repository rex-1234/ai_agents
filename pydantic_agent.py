from pydantic_ai import Agent, RunContext
from tools.internet_search import internet_search


research_agent = Agent(
    "groq:llama-3.3-70b-versatile",
    system_prompt="""
    You are an AI research assistant.
    Use the search_tool to gather information from the internet.
    Then summarize the findings clearly.
    """
)


@research_agent.tool
def search_tool(ctx: RunContext, query: str) -> str:
    """Search the internet for latest information."""
    return internet_search(query)


async def ask_pydantic_agent(question: str):
    result = await research_agent.run(question)
    return result.output
