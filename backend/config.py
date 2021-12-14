from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv('.env')
from decouple import config
import os

secretKey=config('secret')

class Secret(BaseSettings):
    authjwt_secret_key = secretKey

class Settings(BaseSettings): 
    BASE_URL = "http://localhost:8000"
    USE_NGROK = os.environ.get("USE_NGROK", "False") == "True"    