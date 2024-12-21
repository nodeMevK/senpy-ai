import os 
from models import ShortMemory, LongMemory, User
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

pg_key = os.getenv("POSTGRES_KEY")
DB_URL = f"postgresql+psycopg2://"