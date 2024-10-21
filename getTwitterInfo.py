import tweepy



auth = tweepy.OAuth1UserHandler(
    

)

twit = tweepy.API()

public_tweets = twit.home_timeline()

for tweet in public_tweets:
    print(tweet.text)