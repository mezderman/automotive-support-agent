from llama_index.core.workflow import Event
from llama_index.core.schema import NodeWithScore

class RetrieveEvent(Event):
    """Retrieve event (gets retrieved nodes)."""

    retrieved_nodes: list[NodeWithScore]