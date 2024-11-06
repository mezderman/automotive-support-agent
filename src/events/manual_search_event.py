from llama_index.core.workflow import Event

class ManualSearchEvent(Event):
    query: str
    manual_result: str
