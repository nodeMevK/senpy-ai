''' file to run bot continuously '''

from twitterScraper import GScraper
from agent import TwitterAgent
from characters import ch1
#from database import dbSetup
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

cookies = {
    "ct0": os.getenv("TWIT_COOKIE"),
    "auth_token": os.getenv("TWIT_AUTH_TOKEN")
}

Jaine = TwitterAgent(ch1.skizo, "example_deepseek", "deepseek-r1:1.5b")

#Jaine.generateStreamResponse


mrScrape = GScraper(cookies)


