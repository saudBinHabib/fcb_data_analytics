import logging
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Create log directory if it doesn't exist
LOG_DIR = os.path.join(os.path.dirname(__file__), "log")
os.makedirs(LOG_DIR, exist_ok=True)

# Set up logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)

# Set up file handler
LOG_FILE = os.path.join(LOG_DIR, "app.log")
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(LOG_LEVEL)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

# Add file handler to the root logger
logging.getLogger().addHandler(file_handler)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
