import os
import logging

# Default values
DEFAULT_API_PORT = 8000

# Logger
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("Logger")

# Environment variables
try:
    API_PORT = int(os.getenv("API_PORT", DEFAULT_API_PORT))
except (TypeError, ValueError):
    API_PORT = DEFAULT_API_PORT
