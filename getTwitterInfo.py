import tweepy
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

#print(os.getenv("TWITTER_CLIENT"))

auth = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_CLIENT"),
    os.getenv("TWITTER_SECRET"),
    os.getenv("TWIT_ACCESS_TOKEN"),
    os.getenv("TWIT_ACCESS_SECRET")

)

client = tweepy.Client(
    bearer_token=os.getenv("BEARER_TOKEN"),

    consumer_key=os.getenv("TWITTER_CLIENT"),
    consumer_secret=os.getenv("TWITTER_SECRET"),
    access_token=os.getenv("TWIT_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWIT_ACCESS_SECRET")

)

#twit = tweepy.API(auth)

public_tweets = client.get_home_timeline()

#public_tweets = twit.home_timeline()

for tweet in public_tweets:
    print(tweet.text)