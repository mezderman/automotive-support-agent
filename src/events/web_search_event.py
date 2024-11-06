from llama_index.core.workflow import Event

class WebSearchEvent(Event):
    query: str
    web_results: list
