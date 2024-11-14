from twitter.scraper import Scraper
from twitter.util import init_session 
from twitter.account import Account

import os
from dotenv import load_dotenv, find_dotenv
import pandas as pd
import json

load_dotenv(find_dotenv())

def getUserId(username):
    result = scraper.users([username])
    return result[0]['data']['user']['result']['rest_id']

def getTweets(id):
    result = scraper.tweets(id)
    return result

def organizeTweetData(tweets):
    df = pd.json_normalize(tweets[0])
    return df


def getUserId2(username):
    result = scraper.users([username])


def getTweetText(tweet):
    text = tweet[0]['data']['user']['result']
    return text

cookies = {
    "ct0": os.getenv("TWIT_COOKIE"),
    "auth_token": os.getenv("TWIT_AUTH_TOKEN")
}

'''scraper = Scraper(cookies=)'''


#account = Account(cookies=cookies)
scraper = Scraper(cookies=cookies)

'''tg = scraper.users(['notthreadguy'])
print(tg)'''

#print(getTweets("notthreadguy"))
#print(getUserId("notthreadguy"))
#print(getUserId(""))

tweets = scraper.tweets([1426732252768182281],limit=1)
#print(tweets)
'''print("this is df")
print("\n\n")

newDf = organizeTweetData(tweets).head()'''
'''newDf.to_csv('myDataFrame.csv')


print("this is rest_id")
print(newDf['rest_id'])'''

new_tweet = getTweetText(tweets)
#print("this is new_tweet")
#print(new_tweet)

print(len(tweets[0]))

#print(tweets[0])


for entry in new_tweet['timeline_v2']['timeline']['instructions'][1]['entry']['content']:
    print(entry)
    print("\n")

print(len(new_tweet['timeline_v2']['timeline']['instructions']))
'''for value in new_tweet['timeline_v2'].values():
    print(value)
    print("\n\n")'''

'''with open('tweetData.txt', 'w') as file:
    json.dump(new_tweet, file)  '''  

#print(account.home_latest_timeline(1))

