from llama_index.core.workflow import Event

class GenerateResponseEvent(Event):
    response: str
