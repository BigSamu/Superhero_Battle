import os
import logging
from dotenv import load_dotenv

# Load environmental variables from .env file
load_dotenv()

# Define constants
SUPERHERO_API_KEY = os.getenv("SUPERHERO_API_KEY")
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN_NAME = os.getenv("MAILGUN_DOMAIN_NAME")
SUPERHERO_API_URL = f"https://superheroapi.com/api/{SUPERHERO_API_KEY}"
MAILGUN_API_URL = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN_NAME}/messages"
ROOT_DIRECTORY_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
)

# Configure logging
logging.basicConfig(
    format="%(message)s",
    level=logging.INFO,
    filename="battle_log.txt",
    filemode="w",
)
