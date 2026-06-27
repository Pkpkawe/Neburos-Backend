from pathlib import Path
from os.path import join
from pydantic_settings import BaseSettings , SettingsConfigDict

#path
BASE_DIR = Path(__file__).parent.parent.parent.parent
DOT_ENV_FILE_PATH = join(BASE_DIR , ".env")
PROJECT_DIR = join(BASE_DIR , "src")

#configs
class Settings(BaseSettings):
    #general
    DEBUG : bool = False
    
    # Database
    #DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=DOT_ENV_FILE_PATH)

settings = Settings()