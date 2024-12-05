from database import db

class ShortMemory(db.Model):
    __tablename__ = 'short_term_memory'

class LongMemory(db.Model):
    __tablename__ = "long_term_memory"

class User(db.Model):
    __tablename__ = "user"

class Tweets(db.Model):
    __tablename__ = "tweets_from_user_scrape"

class TimeLineTweets(db.Model):
    __tablename__ = "time_line_tweets"

    