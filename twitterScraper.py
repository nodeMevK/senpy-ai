from twitter.scraper import Scraper
from twitter.util import init_session 
from twitter.account import Account

import os
from dotenv import load_dotenv, find_dotenv
import pandas as pd
import json

load_dotenv(find_dotenv())

def getUserId(username):
    ''' get id of twitter user '''
    result = scraper.users([username])
    return result[0]['data']['user']['result']['rest_id']

def getTweets(id):
    result = scraper.tweets(id)
    return result

def organizeTweetData(tweets):
    ''' Organize tweets into a pandas dataframe '''
    df = pd.json_normalize(tweets[0])
    return df


def getUserId2(username):
    result = scraper.users([username])


def getTweetText(tweet):
    text = tweet[0]['data']['user']['result']
    return text

def getTweetInfo():
    '''res = {
        "handle": "",
        "tweet": "",
        "tweet_id": "",
        "timestamp": ""
    }'''

    res_arr = []

    num = 1

    for entry in new_tweet['timeline_v2']['timeline']['instructions'][2]['entries']:
        res = {
            "handle": "",
            "tweet": "",
            "tweet_id": "",
            "timestamp": ""
        }
        try:
            #print(type(entry))
            if (entry['entryId'][:5] == "tweet"):
                print(str(num) + ": " + entry['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])
                num += 1

                ''' At this point need to get other data in legacy as well '''
                ''' maybe some dictionary comprehension or add straight to a db '''

            else:

                # TODO

                print("either a reply or something else .. ")
            #res["tweet"] = entry['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
            #res_arr.append(res)
        except KeyError as e:
            print(e)
            continue
                    
    return res_arr
    

cookies = {
    "ct0": os.getenv("TWIT_COOKIE"),
    "auth_token": os.getenv("TWIT_AUTH_TOKEN")
}

'''scraper = Scraper(cookies=)'''


#account = Account(cookies=cookies)
scraper = Scraper(cookies=cookies)

'''tg = scraper.users(['notthreadguy'])
print(tg)'''



#tweets = scraper.tweets([1426732252768182281],limit=100)
tweets = scraper.tweets([1426732252768182281])

'''print("this is df")
print("\n\n")

newDf = organizeTweetData(tweets).head()'''
'''newDf.to_csv('myDataFrame.csv')


print("this is rest_id")
print(newDf['rest_id'])'''

new_tweet = getTweetText(tweets)
'''print("this is new_tweet")
print(new_tweet)'''


#print(tweets[0])


'''for entry in new_tweet['timeline_v2']['timeline']['instructions'][2]['entries']:
    print(type(entry))
    print(entry['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])
    #for _ in len(entry):
        #print(content['itemContent']['tweet_results']['result']['legacy']['full_text'])
    #print(entry)
    #print("\n\n\n\n")'''
    

#print(len(new_tweet['timeline_v2']['timeline']['instructions']))
'''for value in new_tweet['timeline_v2'].values():
    print(value)
    print("\n\n")'''

'''with open('tweetData.txt', 'w') as file:
    json.dump(new_tweet, file) '''  

#print(account.home_latest_timeline(1))

getTweetInfo()