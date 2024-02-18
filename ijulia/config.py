from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    status: bool = False
    sleep_time: float = 0.1
    

settings = Settings()