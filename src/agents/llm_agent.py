from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage
from llama_index.core.memory import ChatMemoryBuffer
from src.utils import load_prompt_template
import os

class LLMAgent:
    def __init__(self):
        # Initialize the LLM client with llama_index's OpenAI wrapper
        self.client = OpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))
        self.memory = ChatMemoryBuffer.from_defaults(llm=self.client)  # Memory buffer to store chat history

    async def respond_to_query(self, docs, query):
        self.memory.put(ChatMessage(role="user", content=query))
        prompt_text = load_prompt_template("summary_template", documents=docs, query=query)

        # Retrieve previous chat history from memory
        messages = self.memory.get() + [ChatMessage(role="user", content=prompt_text)]

        
        response = await self.client.achat(messages=messages)

        self.memory.put(ChatMessage(role="assistant", content=response.message.content))
        mem = self.memory.get()
        print(mem)
        return response.message.content
