from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Enterprise AI Knowledge Platform"
    environment: str = "development"
    debug: bool = True

    openai_api_key: str
    pinecone_api_key: str
    pinecone_environment: str
    pinecone_index_name: str

    class Config:
        env_file = ".env"


settings = Settings()
