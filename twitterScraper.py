from twitter.scraper import Scraper
from twitter.util import init_session 
from twitter.account import Account

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def getUserId(username):
    result = scraper.users([username])
    return result[0]['data']['user']['result']['rest_id']

def getTweets(id):
    result = scraper.tweets(id)
    return result


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
print(getUserId("notthreadguy"))
#print(getUserId(""))

tweets = scraper.tweets([1426732252768182281],limit=1)
print(tweets)

#print(account.home_latest_timeline(1))

