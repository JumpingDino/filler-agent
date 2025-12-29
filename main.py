import os
from pathlib import Path
from dotenv import load_dotenv


def main():
    print("Hello from filler-agent!")

    # Load environment variables from .env file
    env_path = Path(__file__).parent / ".env"
    load_dotenv(dotenv_path=env_path)

    # API Keys
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


if __name__ == "__main__":
    main()
