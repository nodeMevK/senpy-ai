''' file to make initial dbs'''


from models import ShortMemory, LongMemory, User
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
from database.dbSetup import Session, engine


''' need to get to this asap'''
session = Session()
def addToShortTerm(record):

    session.add(record)
    session.commit()
    return

def addToLongTerm(record):

    session.add(record)
    session.commit()
    return

def makeShortEntry(data):
    record = ShortMemory(
        id = data["id"],
        post = data["post"],
    )
    

    return record 

def makeLongEntry(data):
    record = LongMemory(
        id = data["id"],
        post = data["post"],
    )
    return record 