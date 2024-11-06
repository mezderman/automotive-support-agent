# src/tools/user_tool.py
from typing import Dict, Optional
from llama_index.tools import BaseTool
from ..utils.logger import setup_logger

logger = setup_logger(__name__)

class UserProfileTool(BaseTool):
    """Tool for retrieving user profile information."""
    
    name = "User Profile Tool"
    description = "Retrieves user profile information including their vehicle details and maintenance history"

    def __init__(self, api_endpoint: str):
        """
        Initialize the UserProfileTool.
        
        Args:
            api_endpoint (str): The API endpoint for user data (not used in this mock version)
        """
        super().__init__()
        self.api_endpoint = api_endpoint
        # Mock user database
        self.mock_users = {
            "user123": {
                "personal_info": {
                    "name": "John Doe",
                    "email": "john.doe@example.com",
                    "preferred_language": "English"
                },
                "vehicle_info": {
                    "make": "Toyota",
                    "model": "Camry",
                    "year": 2020,
                    "trim": "SE",
                    "vin": "1HGCM82633A123456"
                },
                "maintenance_history": [
                    {
                        "date": "2023-12-15",
                        "service_type": "Oil Change",