import os

from dotenv import load_dotenv

load_dotenv(override=True)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

LLM_PROVIDER = str(os.getenv("LLM_PROVIDER"))
OPENROUTER_MODEL = str(os.getenv("OPENROUTER_MODEL"))