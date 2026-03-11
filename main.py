import asyncio
from pydantic_agent import ask_pydantic_agent
from crewai_agents import run_crewai


async def main():

    question = input("Enter your research question: ")

    print("\n--- PydanticAI Agent ---\n")

    pydantic_answer = await ask_pydantic_agent(question)
    print(pydantic_answer)

    print("\n--- CrewAI Multi-Agent ---\n")

    crew_answer = run_crewai(question)
    print(crew_answer)


if __name__ == "__main__":
    asyncio.run(main())
