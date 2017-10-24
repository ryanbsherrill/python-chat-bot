import tweepy => 
from time import sleep # time lib => sys sleep
from credentials import *

# set up auth with tweepy
#helps it know it's johnBot
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#acces to johnBot
auth.set_access_token(access_token, access_token_secret)
#call to our api and pass in credentials
api = tweepy.API(auth)
# open book => r is for read only
mobydick = open('mobydick.txt', 'r')
# read line(s) from book
mobydick_lines = mobydick.readlines();
# close file read stream
mobydick.close()

for line in mobydick_lines:
  # catch errors for duplicate tweets
  try:
    # no errors will tweet
    # print(line)
    # if line is not a blank tweet
    if line != '\n':
      print('tweeting some line')
      api.update_status(line)
    # if line is blank don't tweet
    else:
      print('blank line yo')
      pass
  # handles the error
  except tweepy.TweepError as e:
    print(e.reason)
  print('going to sleep')
  sleep(5)