import requests
from bs4 import BeautifulSoup


def internet_search(query: str) -> str:
    """
    Simple internet search tool.
    Fetches top search results and returns combined snippets.
    """

    url = f"https://duckduckgo.com/html/?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for result in soup.select(".result")[:5]:
        title = result.select_one(".result__title")
        snippet = result.select_one(".result__snippet")
        if title and snippet:
            results.append(f"{title.get_text(strip=True)}: {snippet.get_text(strip=True)}")

    return "\n\n".join(results) if results else "No results found."
