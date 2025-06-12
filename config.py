# config.py
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    bot_token: str
    database_path: str  # 👈 shu qatorni qo‘shish kerak

    class Config:
        env_file = ".env"

settings = Settings()





