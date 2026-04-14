from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URL: str
    DATABASE_NAME: str
    
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()