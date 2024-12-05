from database import db

class ShortMemory(db.Model):
    __tablename__ = 'short_term_memory'
    id = db.Column(db.Integer, primary_key=True)


class LongMemory(db.Model):
    __tablename__ = "long_term_memory"
    id = db.Column(db.Integer, primary_key=True)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)


class Tweets(db.Model):
    __tablename__ = "tweets_from_user_scrape"
    id = db.Column(db.Integer, primary_key=True)


class TimeLineTweets(db.Model):
    __tablename__ = "time_line_tweets"
    id = db.Column(db.Integer, primary_key=True)


