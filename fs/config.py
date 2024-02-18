from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    status: bool = False
    

settings = Settings()