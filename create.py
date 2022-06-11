import tweepy
import config
client = tweepy.Client(consumer_key=config.API_KEY,
                        consumer_secret=config.API_SECRET,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET)
response=client.retweet(tweet_id='1508554204901687305')
print(response)