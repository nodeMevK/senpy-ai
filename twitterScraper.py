from twitter.scraper import Scraper
from twitter.util import init_session 
from twitter.account import Account
import os
import json
from dotenv import load_dotenv, find_dotenv
import pandas as pd

load_dotenv(find_dotenv())

def getUserId(username):
    ''' get id of twitter user '''
    result = scraper.users([username])
    return result[0]['data']['user']['result']['rest_id']

def getTweets(id):
    '''get a list of tweets from a user'''
    result = scraper.tweets(id)
    return result

def organizeTweetData(tweets):
    ''' Organize tweets into a pandas dataframe '''
    df = pd.json_normalize(tweets[0])
    return df

def getUserId2(username):
    result = scraper.users([username])


def getTweetText(tweet):
    '''get '''
    text = tweet[0]['data']['user']['result']
    return text

def getTweetInfo(tweetList):
    res_arr = []

    for entry in tweetList['timeline_v2']['timeline']['instructions'][2]['entries']:
        res = {
            "user_name": "",
            "name": "",
            "tweet": "",
            "tweet_id": "",
            "timestamp": ""
        }
        try:
            if (entry['entryId'][:5] == "tweet"):
               
                ''' At this point need to get other data in legacy as well '''
                ''' maybe some dictionary comprehension or add straight to a db '''
                entry_result = entry['content']['itemContent']['tweet_results']['result']
                legacy = entry_result['legacy']
                core = entry_result['core']


                ''' user info is in core layer '''
                res["user_name"] = core["user_results"]["result"]["legacy"]["screen_name"]
                res["name"] = core["user_results"]["result"]["legacy"]["name"]

                res["tweet"] = legacy["full_text"]
                res["tweet_id"] = legacy["id_str"]
                res["timestamp"] = legacy["created_at"]

                res_arr.append(res)
             
            else:

                # TODO

                print("either a reply or something else .. ")
        except KeyError as e:
            print(e)
            continue

    return res_arr
    

cookies = {
    "ct0": os.getenv("TWIT_COOKIE"),
    "auth_token": os.getenv("TWIT_AUTH_TOKEN")
}

scraper = Scraper(cookies=cookies)


tweets = scraper.tweets([getUserId("notthreadguy")], limit=10)
new_tweet = getTweetText(tweets)

with open('tweetData.txt', 'w') as file:
    json.dump(new_tweet, file)


final = getTweetInfo(new_tweet)
print(len(final))
for section in final:
    print(section)