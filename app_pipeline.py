''' file to run bot continuously '''

from twitterScraper import GScraper
from agent import TwitterAgent
from characters.ch1 import skizo as skitz
#from database import dbSetup
from dotenv import load_dotenv, find_dotenv
from database.dbSetup import getDb
import os

load_dotenv(find_dotenv())

cookies = {
    "ct0": os.getenv("TWIT_COOKIE"),
    "auth_token": os.getenv("TWIT_AUTH_TOKEN")
}

Jaine = TwitterAgent(skitz, "example_deepseek", "deepseek-r1:1.5b")

#Jaine.generateStreamResponse

mrScrape = GScraper(cookies)

def main():
    try:
        pass
    except KeyboardInterrupt:
        print("Process over") 

if __name__ == "__main__":
    main()

