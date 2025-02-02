from dotenv import load_dotenv
import os
from sqlalchemy import create_engine,text

load_dotenv() #Load .env
DB_URL=os.getenv("DB_URL") # DB URL from .env file

engine=create_engine(
    url=DB_URL,
    echo=True,
    pool_size=5,
    max_overflow=10
)


