from openai import OpenAI
import os


class LLMAgent:
    def __init__(self):
        # Set your OpenAI API key
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-3.5-turbo"  # Use GPT-4 or other models if available

    def respond_to_query(self, query):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message.content
        
    
    

