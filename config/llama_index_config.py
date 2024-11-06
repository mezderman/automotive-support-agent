# config/config.py
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # API Configurations
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    USER_API_ENDPOINT = os.getenv("USER_API_ENDPOINT")
    
    # RAG Configurations
    MANUAL_DATA_PATH = os.path.join("data", "car_manuals")
    
    # Logging Configuration
    LOG_PATH = os.path.join("logs", "app.log")
    LOG_LEVEL = "INFO"
    
    # Agent Configuration
    MODEL_NAME = "gpt-4"  # or your preferred model
    TEMPERATURE = 0.7
    MAX_TOKENS = 1000