from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str):
    """Searches for Linkedin or Twitter Profile Page."""
    search = TavilySearchResults()
    result = search.run(f"site:linkedin.com AND {name}")
    
    return result[0]["url"]
