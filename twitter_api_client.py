import os
import sys
from tweepy import API #tweepy is the python-twitter api helper thing
from tweepy import OAuthHandler

# TWITTER_CONSUMER_KEY = "INSERT YOUR OWN"
# TWITTER_CONSUMER_SECRET = "INSERT YOUR OWN"
# TWITTER_ACCESS_TOKEN = "INSERT YOUR OWN"
# TWITTER_ACCESS_SECRET = "INSERT YOUR OWN"

def get_twitter_auth(): #initializing all the stuff
  try:
    # consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
    # consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
    # access_token = os.environ["TWITTER_ACCESS_TOKEN"]
    # access_secret = os.environ["TWITTER_ACCESS_SECRET"]
    consumer_key = "INSERT YOUR OWN"
    consumer_secret = "INSERT YOUR OWN"
    access_token = "INSERT YOUR OWN"
    access_secret = "INSERT YOUR OWN"

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
