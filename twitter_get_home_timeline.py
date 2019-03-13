import json
from tweepy import Cursor
from twitter_api_client import get_twitter_client

if __name__ == "__main__": #basically just runs all the functions
  client = get_twitter_client() #getting info from previous file

  with open("home_timeline.json1", "w") as f: #opening file, writing to it
    for page in Cursor(client.home_timeline, count = 200).pages(4): #returning past 200 tweets from feed(?)
      for status in page:
        f.write(json.dumps(status._json) + "\n") #writing it all to a returned json file



  # for status in Cursor(client.home_timeline).items(10):
  #   print(status.text)
