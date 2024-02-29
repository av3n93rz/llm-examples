import os
import logging
from dotenv import load_dotenv

load_dotenv()

# Default values
DEFAULT_API_PORT = 8000

# Logger
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Environment variables
POSTGRES_CONNECTION_STRING = os.getenv("POSTGRES_URL")
try:
    API_PORT = int(os.getenv("API_PORT", DEFAULT_API_PORT))
except (TypeError, ValueError):
    API_PORT = DEFAULT_API_PORT

## Api keys
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
