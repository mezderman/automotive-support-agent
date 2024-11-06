import os
import sys

# Add the 'src' directory to sys.path if running from the root directory
sys.path.insert(0, os.path.abspath("src"))

from workflows.car_assistant_workflow import CarAssistantWorkflow
from llama_index.utils.workflow import draw_all_possible_flows

# Draw and save the workflow visualization to an HTML file
draw_all_possible_flows(CarAssistantWorkflow, filename="basic_workflow.html")

print("Workflow visualization saved as 'basic_workflow.html'")
