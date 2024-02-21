from pydantic_settings import BaseSettings, SettingsConfigDict
import sys
import os
from pathlib import Path
 
#BASE_DIR = Path(os.path.realpath(__file__)).parent.parent
#sys.path.append(BASE_DIR)

class Settings(BaseSettings):
    DB_HOST : str
    DB_PORT : int
    DB_USER : str
    DB_PASSWORD : str
    DB_NAME : str

    @property
    def database_url_asyncpg(self):
        # postgresql+asyncpg://postgres:postgres@localhost:5432/sa
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @property
    def database_url_psycopg(self):
        # postgresql+psycopg://postgres:postgres@localhost:5432/sa
        return f'postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    #model_config = SettingsConfigDict(env_file=Path(BASE_DIR, ".env"))

    model_config = SettingsConfigDict(env_file=".env")

setting = Settings()

