from llama_index.core.workflow import Event
from llama_index.core.schema import NodeWithScore

class GenerateResponseEvent(Event):
    response: str

class ManualSearchEvent(Event):
    query: str
    manual_result: str


class InitialQueryEvent(Event):
    def __init__(self, query):
        self.query = query


class SummaryConfirmationEvent(Event):
    def __init__(self, summary, confirmed):
        self.summary = summary
        self.confirmed = confirmed
        
class RetrieveEvent(Event):
    """Retrieve event (gets retrieved nodes)."""

    retrieved_nodes: list[NodeWithScore]

class UserProfileEvent(Event):
    user_profile: dict

class WebSearchEvent(Event):
    query: str
    web_results: list