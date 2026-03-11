from crewai import Agent, Task, Crew
from crewai.tools import tool
from dotenv import load_dotenv
from tools.internet_search import internet_search


load_dotenv()  # Load environment variables from .env file


@tool("search_tool")
def search_tool(query: str) -> str:
    """
    Search the internet using DuckDuckGo and return top results.

    Args:
        query: search query string

    Returns:
        Top search results summary
    """
    return internet_search(query)


research_agent = Agent(
    role="AI research assistant",
    goal="Find useful information on the internet.",
    backstory="Expert researcher skilled in gathering information.",
    tools=[search_tool],
    llm="groq/llama-3.1-8b-instant",
    verbose=True,
    allow_delegation=False
)


summarizer_agent = Agent(
    role="Content Summarizer",
    goal="Summarize research into clear insights",
    backstory="Expert at writing clear summaries.",
    llm="groq/llama-3.1-8b-instant",
    verbose=True
)


def run_crewai(question: str):

    research_task = Task(
        description=f"""
            Research the following topic: {question}

            You have access to ONLY one tool: search_tool.

            Use search_tool to search the internet.
            Do NOT attempt to use any other tool.

            After using search_tool, analyze the results and produce detailed research findings.
            """,
        agent=research_agent,
        expected_output="Detailed research findings from the internet."

    )

    summary_task = Task(
        description="Summarize the research findings into a concise explanation.",
        agent=summarizer_agent,
        expected_output="A clear and concise summary of the research findings.",
        context=[research_task]
    )

    crew = Crew(
        agents=[research_agent, summarizer_agent],
        tasks=[research_task, summary_task],
        process="sequential",
        verbose=True
    )

    result = crew.kickoff()

    return result
