from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ShortMemory(Base):
    __tablename__ = "short_term_memory"

    id = Column(Integer, primary_key=True, index=True)
    post = Column(String, index=True)


class LongMemory(Base):
    __tablename__ = "long_term_memory"

    id = Column(Integer, primary_key=True)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    user_id = Column(Integer)


class Tweets(Base):
    __tablename__ = "tweets_from_user_scrape"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    tweet = Column(String)
    tweet_id = Column(Integer)
    time_stamp = Column(DateTime(timezone=True))



class TimeLineTweets(Base):
    __tablename__ = "time_line_tweets"
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    tweet = Column(String)
    tweet_id = Column(Integer)
    time_stamp = Column(DateTime(timezone=True))


