from crewai import Agent, Task, Crew
from crewai.tools import tool
from langchain_groq import ChatGroq
from tools.internet_search import internet_search


# LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


@tool("search_tool")
def search_tool(query: str) -> str:
    return internet_search(query)


research_agent = Agent(
    role="AI research assistant",
    goal="Find useful information on the internet.",
    backstory="Expert researcher skilled in gathering information.",
    tools=[search_tool],
    llm=llm,
    verbose=True
)


summarizer_agent = Agent(
    role="Content Summarizer",
    goal="Summarize research into clear insights",
    backstory="Expert at writing clear summaries.",
    llm=llm,
    verbose=True
)


def run_crewai(question: str):

    research_task = Task(
        description=f"Research the following topic using the internet: {question}",
        agent=research_agent
    )

    summary_task = Task(
        description="Summarize the research findings into a concise explanation.",
        agent=summarizer_agent
    )

    crew = Crew(
        agents=[research_agent, summarizer_agent],
        tasks=[research_task, summary_task],
        verbose=True
    )

    result = crew.kickoff()

    return result
