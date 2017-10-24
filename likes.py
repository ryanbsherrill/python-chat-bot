import tweepy
from time import sleep # time lib => sys sleep
from credentials import *

# set up auth with tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

js_tweets = tweepy.Cursor(api.search, q='#javascript', lang='en').items(2)

for tweet in js_tweets:
  try:
    print('tweeted by @%s' % tweet.user.screen_name)
    tweet.retweet()
    print('retweeted the tweet!')
    sleep(10)
  except tweepy.TweepError as e:
    print(e.reason)
  except StopIteration:
    print('stopping the bot')
    break
