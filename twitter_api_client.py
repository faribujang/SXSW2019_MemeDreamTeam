import os
import sys
from tweepy import API #tweepy is the python-twitter api helper thing
from tweepy import OAuthHandler

# TWITTER_CONSUMER_KEY = "j0zhTcAe9pM4wwtSCJwaVCh89"
# TWITTER_CONSUMER_SECRET = "ckYkM1dV4CyOhIY408k2keJgJ3BfsNmuwQbMGmzWMk0VzBI0Kk"
# TWITTER_ACCESS_TOKEN = "825406380161036289-Y1wsMZ1kYzRRrg2SDqUkMe1coDU0NTN"
# TWITTER_ACCESS_SECRET = "mWChjTWuUwnsO7VsOVxG9XvDrRgDOGReasxj7fY94w9H4"

def get_twitter_auth(): #initializing all the stuff
  try:
    # consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
    # consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
    # access_token = os.environ["TWITTER_ACCESS_TOKEN"]
    # access_secret = os.environ["TWITTER_ACCESS_SECRET"]
    consumer_key = "j0zhTcAe9pM4wwtSCJwaVCh89"
    consumer_secret = "ckYkM1dV4CyOhIY408k2keJgJ3BfsNmuwQbMGmzWMk0VzBI0Kk"
    access_token = "825406380161036289-Y1wsMZ1kYzRRrg2SDqUkMe1coDU0NTN"
    access_secret = "mWChjTWuUwnsO7VsOVxG9XvDrRgDOGReasxj7fY94w9H4"

  except KeyError: #if the keys dont return an acceptable value, return error code
    sys.stderr.write("TWITTER_* environment variables not set \n")
    sys.exit(1)
  auth = OAuthHandler(consumer_key, consumer_secret) #authorization functions from tweepy
  auth.set_access_token(access_token, access_secret)
  return auth

def get_twitter_client(): #running all the stuff
  auth = get_twitter_auth()
  client = API(auth)
  return client
