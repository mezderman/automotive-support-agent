
import asyncio
import sys
import os
from dotenv import load_dotenv
sys.path.insert(0, os.path.abspath("src"))

from src.workflows.car_assistant_workflow import CarAssistantWorkflow

# Load environment variables from .env file at the start
load_dotenv()

async def main():
    workflow = CarAssistantWorkflow(timeout=30, verbose=True)
    query = "how do I use keyless feature?"
    result = await workflow.run(query=query)
    print("Workflow Result:", result)

if __name__ == "__main__":
    asyncio.run(main())
