from twitter.scraper import Scraper
from twitter.util import init_session 
from twitter.account import Account
import json
import pandas as pd

class GScraper:

    def __init__(self, _cookies: dict):
        self.scraper = Scraper(cookies=_cookies)
        self.account = Account(cookies=_cookies)
        pass

    def getUserId(self, username: str):
        ''' get id of twitter user '''
        result = self.scraper.users([username])
        #return result[0]
        return result[0]['data']['user']['result']['rest_id']

    def getTweets(self, id):
        '''get a list of tweets from a user'''
        result = self.scraper.tweets([id], limit=10)
        return result

    def organizeTweetData(self, tweets):
        ''' Organize tweets into a pandas dataframe '''
        df = pd.json_normalize(tweets[0])
        return df

    def getUserId2(self, username):
        result = self.scraper.users([username])


    def getTweetText(self, tweet):
        '''get '''
        text = tweet[0]['data']['user']['result']
        return text
    
    def getTimeLineTweets(self):
        timeline = self.account.home_timeline()
        return timeline
        
    def getLatestTl(self, _limit: int):
        latest_tl = self.account.home_latest_timeline(limit=_limit)
        return latest_tl
    
    def getEntries(self, tl_tweets):
        res_arr = []

        text = tl_tweets[0]["data"]["home"]["home_timeline_urt"]["instructions"][0]["entries"]
        for entry in text:
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
        

    def getTweetInfo(self, tweetList):
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
    
    

'''cookies = {
    "ct0": os.getenv("TWIT_COOKIE"),
    "auth_token": os.getenv("TWIT_AUTH_TOKEN")
}'''

#scraper = Scraper(cookies=cookies)

#myScraper = GScraper(cookies)
#userId = myScraper.getUserId("notthreadguy")
#print(userId)
'''tweets = myScraper.scraper.tweets([myScraper.getUserId("notthreadguy")], limit=10)
tweet = myScraper.getTweetText

final = myScraper.getTweetInfo(tweet)
for section in final:
    print(section)'''

'''tweets = scraper.tweets([getUserId("notthreadguy")], limit=10)
new_tweet = getTweetText(tweets)

with open('tweetData.txt', 'w') as file:
    json.dump(new_tweet, file)


final = getTweetInfo(new_tweet)
print(len(final))
for section in final:
    print(section)'''


