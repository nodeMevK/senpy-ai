from twitter.scraper import Scraper
from twitter.util import init_session 

scraper = Scraper(session=init_session())

# get user data
users = scraper.users(['jack'])

print(users)