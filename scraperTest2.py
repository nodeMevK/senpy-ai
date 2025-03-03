import os
from dotenv import load_dotenv, find_dotenv
from twitterScraper import GScraper
from database.dbSeed import *

import json

load_dotenv(find_dotenv())

cookies = {
    "ct0": os.getenv("TWIT_COOKIE"),
    "auth_token": os.getenv("TWIT_AUTH_TOKEN")
}

testScraper = GScraper(_cookies=cookies)

'''testId = testScraper.getUserId("notthreadguy")
tweets = testScraper.getTweets(testId)

newTweets = testScraper.getTweetText(tweets)

final = testScraper.getTweetInfo(newTweets)
print(len(final))
for section in final:
    print(section)'''

#print(testScraper.getTweetText(tweets))


#print(testScraper.getTimeLineTweets())
print("grabbing tweets ...")
tl = testScraper.getLatestTl(1)
print("obtained tweets ...")

final = testScraper.getEntries(tl)
print(len(final))

for section in final:
    makeShortEntry(section)
    print("entry added")
    print(section)

'''print("dumping to file ...")
with open('test.txt', 'w') as file:
    json.dump(tl, file)'''

print("finished ...")