import os 
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "User API"
    API_V1_STR: str = "/api/v1"

    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()
