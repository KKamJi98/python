from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Tutorial"
    debug: bool = True

settings = Settings()
