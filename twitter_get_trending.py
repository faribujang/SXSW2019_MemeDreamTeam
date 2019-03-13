import tweepy
consumer_key = "INSERT YOUR OWN"
consumer_secret = "INSERT YOUR OWN"
access_token = "INSERT YOUR OWN"
access_token_secret = "INSERT YOUR OWN"
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) #TBH IDK HOW THIS STUFF WORKS, IT'S QUERYING FROM THE API MODULE IN TWEEPY PACKAGE
# trends1 = api.trends_place(1)
trends2 = api.trends_closest(30.267153,-97.7430608) #getting stuff from Austin location

print(trends1)
