from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage
import os

class LLMAgent:
    def __init__(self):
        # Initialize the LLM client with llama_index's OpenAI wrapper
        self.client = OpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))

    async def respond_to_query(self, query):
        # Convert the message to ChatMessage format
        messages = [ChatMessage(role="user", content=query)]
        response = await self.client.achat(messages=messages)
        return response.message.content
