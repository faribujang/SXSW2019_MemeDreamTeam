import tweepy
consumer_key = "j0zhTcAe9pM4wwtSCJwaVCh89"
consumer_secret = "ckYkM1dV4CyOhIY408k2keJgJ3BfsNmuwQbMGmzWMk0VzBI0Kk"
access_token = "825406380161036289-Y1wsMZ1kYzRRrg2SDqUkMe1coDU0NTN"
access_token_secret = "mWChjTWuUwnsO7VsOVxG9XvDrRgDOGReasxj7fY94w9H4"
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# trends1 = api.trends_place(1)
trends2 = api.trends_closest(30.267153,-97.7430608)

print(trends1)
