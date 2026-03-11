# AI Agents

A Python project demonstrating two different AI agent frameworks for research and information gathering: **PydanticAI** and **CrewAI**.

## Features

- **PydanticAI Agent**: Single-agent system for research with integrated internet search capabilities
- **CrewAI Multi-Agent**: Coordinated multi-agent system with specialized roles:
  - Research Agent: Gathers information from the internet
  - Summarizer Agent: Distills research into clear insights
- **Internet Search Tool**: DuckDuckGo-powered web search integration
- **LLM Integration**: Uses Groq API with Llama 3.1 8B model

## Prerequisites

- Python 3.13 or higher
- Groq API key (get one at [console.groq.com](https://console.groq.com))

## Installation

1. Clone the repository and navigate to the project directory:

   ```bash
   cd /Users/jitendra/projects/ai_agents
   ```

2. Install dependencies using uv or pip:

   ```bash
   uv sync
   ```

   Or with pip:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the project root with your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

## Usage

Run the main script to interact with both agents:

```bash
python main.py
```

You'll be prompted to enter a research question, and the system will:

1. Process the question through the PydanticAI agent
2. Process the same question through the CrewAI multi-agent system
3. Display results from both approaches

### Example

```
Enter your research question: What are the latest developments in quantum computing?

--- PydanticAI Agent ---
[Agent response with research findings...]

--- CrewAI Multi-Agent ---
[Multi-agent coordinated response...]
```

## Project Structure

```
.
├── main.py                    # Entry point - runs both agent systems
├── pydantic_agent.py          # PydanticAI agent implementation
├── crewai_agents.py           # CrewAI multi-agent system
├── tools/
│   └── internet_search.py     # Web search tool using DuckDuckGo
├── pyproject.toml             # Project configuration and dependencies
└── README.md                  # This file
```

## Dependencies

- **crewai**: Multi-agent orchestration framework
- **pydantic-ai**: Lightweight AI agent framework
- **langchain-groq**: Groq LLM integration
- **beautifulsoup4**: HTML parsing for search results
- **requests**: HTTP library for web requests
- **python-dotenv**: Environment variable management

## How It Works

### PydanticAI Approach

- Single research agent with integrated search tool
- Faster responses for simple queries
- Ideal for straightforward research tasks

### CrewAI Approach

- Two specialized agents working together
- Research agent gathers comprehensive information
- Summarizer agent distills findings into insights
- Better for complex research requiring synthesis

## Environment Variables

The project expects a `.env` file with:

- `GROQ_API_KEY`: Your Groq API key for LLM access

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.
