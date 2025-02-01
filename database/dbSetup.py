import os 
from models import Base, ShortMemory, LongMemory, User
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv

"""
    Might have to make this a class tbh

"""
load_dotenv(find_dotenv())

pg_key = os.getenv("POSTGRES_KEY")
DB_URL = f"postgresql+psycopg2://postgres:{pg_key}@localhost:5432/tweetsai"

engine = create_engine(DB_URL)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(bind=engine)

record = ShortMemory(
    post = "quick test"
)

session.add(record)
session.commit()
session.close()


