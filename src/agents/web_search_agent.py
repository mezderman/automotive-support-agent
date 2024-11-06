class WebSearchAgent:
    def __init__(self):
        # Initialize any necessary configurations or connections
        pass

    def search_web(self, query):
        # Static test data representing a sample web search result
        search_results = {
            "query": query,
            "top_results": [
                {
                    "title": "How to fix a noisy engine",
                    "link": "https://example.com/fix-noisy-engine",
                    "snippet": "If your engine is making unusual noises, it could be due to various issues such as a loose belt or engine misfire..."
                },
                {
                    "title": "Common car engine noises and their causes",
                    "link": "https://example.com/car-engine-noises",
                    "snippet": "Here are the most common reasons for car engine noises and what you can do about them..."
                }
            ]
        }
        return search_results
