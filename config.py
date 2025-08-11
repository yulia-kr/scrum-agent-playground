import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)

# Set OpenAI and Azure variables
OPENAI_MODEL_NAME = os.getenv('OPENAI_API_TYPE')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
AZURE_OPENAI_LLM_DEPLOYMENT_NAME = os.getenv('AZURE_OPENAI_LLM_DEPLOYMENT_NAME')
AZURE_OPENAI_LLM_MODEL_NAME = os.getenv('AZURE_OPENAI_LLM_MODEL_NAME')
