from llama_index.core.workflow import Workflow, step, StartEvent, StopEvent
from src.agents.user_profile_agent import UserProfileAgent
from src.agents.llm_agent import LLMAgent
from src.agents.car_manual_agent import CarManualAgent
from src.agents.web_search_agent import WebSearchAgent
from src.events.user_profile_event import UserProfileEvent
from src.events.manual_search_event import ManualSearchEvent
from src.events.generate_response_event import GenerateResponseEvent
from src.events.retrieval_event import RetrieveEvent
from llama_index.core.workflow import Context
from src.events.web_search_event import WebSearchEvent

from llama_index.core.llms import ChatMessage
from llama_index.core.memory import ChatMemoryBuffer

class CarAssistantWorkflow(Workflow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_agent = UserProfileAgent()
        self.manual_agent = CarManualAgent(manual_dir="data/car_manuals/")
        self.web_search_agent = WebSearchAgent()
        self.llm_agent = LLMAgent()



    @step
    async def get_user_profile(self, ctx: Context, ev: StartEvent) -> UserProfileEvent:
        await ctx.set("query", ev.query)
        user_profile = self.user_agent.get_user_profile()
        return UserProfileEvent(user_profile=user_profile)

    @step
    async def search_manual(self, ctx: Context, ev: UserProfileEvent) -> RetrieveEvent | ManualSearchEvent:
        query = await ctx.get("query")
        nodes = self.manual_agent.search_manual(query)
        
        # If a result is found in the manual, produce GenerateResponseEvent
        if nodes:
            await ctx.set("retrieved_nodes", nodes)
            return RetrieveEvent(retrieved_nodes=nodes)
        
        # Otherwise, produce ManualSearchEvent to continue the workflow
        return ManualSearchEvent(query=query)

    @step
    async def eval_retriever(self, ev: RetrieveEvent) -> GenerateResponseEvent :
        docs = ""
        nodes = ev.retrieved_nodes
        # Iterate over the nodes with their index
        for i, node in enumerate(nodes, start=1):
        # Append the formatted text to the docs string
            docs += f"DOC_{i}: {node.text}\n"
        return GenerateResponseEvent(response=docs)
    @step
    async def search_web(self, ev: ManualSearchEvent) -> GenerateResponseEvent :
        web_results = self.web_search_agent.search_web(ev.query)
        
        # If web search yields results, produce GenerateResponseEvent
        if web_results:
            return GenerateResponseEvent(response=web_results)
        
        # If no results from web search, produce WebSearchEvent to continue to LLM
        return GenerateResponseEvent(response="no web results")

    @step
    async def generate_response(self, ctx: Context, ev:  GenerateResponseEvent) -> StopEvent:
        # If a GenerateResponseEvent is already produced, conclude with it
        
        
        # If coming from WebSearchEvent, use LLM to generate the final response
        # Load and format the prompt template with the query
        query = await ctx.get("query")
       
        response = await self.llm_agent.respond_to_query(str(ev.response), query)
        
        return StopEvent(result=response)
