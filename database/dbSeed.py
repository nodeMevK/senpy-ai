''' file to make initial dbs'''


from models import ShortMemory, LongMemory, User, TimeLineTweets, Tweets
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

def insertTlTweet(data):
    record = TimeLineTweets(
        username = data["user_name"],
        name = data["name"],
        post = data["tweet"],
        timestamp = data["timestamp"]    
    )
    addToDb(record)


def insertTweet(data):
    record = Tweets(
        username = data["user_name"],
        name = data["name"],
        post = data["tweet"],
        timestamp = data["timestamp"] 
    )
    addToDb(record)


# havent clearly made a section in scraper class to create a dictionary with username and id
def insertUser(data):
    record = User(
        username = data["username"],
        user_id = data["user_id"]
    )
    addToDb(record)

def insertLike(data):
    record = ()
    addToDb(record)

def insertComment(data):
    record = ()
    addToDb(record)

def insertLike(data):
    record = ()
    addToDb(record)
    