''' file to make initial dbs'''


from models import ShortMemory, LongMemory, User
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
from database.dbSetup import Session, engine


''' need to get to this asap'''
session = Session()
def addToDb(record):

    session.add(record)
    session.commit()
    print("Record Added to DB")
    #return


def makeShortEntry(data):
    record = ShortMemory(
        tweet_id = data["tweet_id"],
        username = data["user_name"],
        name = data["name"],
        post = data["tweet"],
        timestamp = data["timestamp"]
    )
    addToDb(record)
    #return record 

def makeLongEntry(data):
    record = LongMemory(
        tweet_id = data["tweet_id"],
        username = data["user_name"],
        name = data["name"],
        post = data["tweet"],
        timestamp = data["timestamp"]
    )
    addToDb(record)
    #return record 