''' file to make initial dbs'''


from models import ShortMemory, LongMemory, User
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
from database.dbSetup import Session, engine


''' need to get to this asap'''

