import tweepy
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

#print(os.getenv("TWITTER_CLIENT"))

'''auth = tweepy.OAuth1UserHandler(
    os.getenv("TWIT_API_KEY"),
    os.getenv("TWIT_API_SECRET"),
    os.getenv("TWIT_ACCESS_TOKEN"),
    os.getenv("TWIT_ACCESS_SECRET")

)
'''


client = tweepy.Client(
    bearer_token=os.getenv("BEARER_TOKEN"),

    consumer_key=os.getenv("TWIT_API_KEY"),
    consumer_secret=os.getenv("TWIT_API_SECRET"),
    access_token=os.getenv("TWIT_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWIT_ACCESS_SECRET")

)



#twit = tweepy.API(auth)

#public_tweets = client.get_home_timeline()

#public_tweets = twit.home_timeline()

'''for tweet in public_tweets:
    print(tweet.text)'''

me = client.get_me()

print(me)