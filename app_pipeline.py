''' file to run bot continuously '''

from twitterScraper import GScraper
from agent import TwitterAgent
from characters.ch1 import skizo as skitz
#from database import dbSetup
from dotenv import load_dotenv, find_dotenv
from database.dbSetup import getDb
import os

def main():
    load_dotenv(find_dotenv())

    cookies = {
        "ct0": os.getenv("TWIT_COOKIE"),
        "auth_token": os.getenv("TWIT_AUTH_TOKEN")
    }

    ''' Create agents '''

    #Jaine = TwitterAgent(skitz, "example_deepseek", "deepseek-r1:1.5b")
    Jaine = TwitterAgent(skitz, "example_latest", "llama3.2:latest", 20)

    #Jaine.generateStreamResponse("Why can't you answer my question about how you are doing?")
    Jaine.generateStreamResponse("What's your take on the crypto market right now?")

    mrScrape = GScraper(cookies)



    ''' pull references from db and place in memory locations  '''


    ''' start tweeting things '''

'''def main():
    try:
        pass
    except KeyboardInterrupt:
        print("Process over") '''

if __name__ == "__main__":
    print("running main")
    main()