import tweepy
consumer_key = "j0zhTcAe9pM4wwtSCJwaVCh89"
consumer_secret = "ckYkM1dV4CyOhIY408k2keJgJ3BfsNmuwQbMGmzWMk0VzBI0Kk"
access_token = "825406380161036289-Y1wsMZ1kYzRRrg2SDqUkMe1coDU0NTN"
access_token_secret = "mWChjTWuUwnsO7VsOVxG9XvDrRgDOGReasxj7fY94w9H4"
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
trends1 = api.trends_place(1)
# trends2 = api.trends_closest(30.267153,-97.7430608)

# print(trends1)
# input_dict = trends1

# track = {}
# for key,value in input_dict.items():
#     if value not in track:
#         track[value]=0
#     else:
#         track[value]+=1

# print(max(track,key=track.get))

# from collections import Counter

# most_common_hashtag_value = Counter(d['name'] for d in trends1).most_common(1)[0]
# print(most_common_hashtag_value)

trends1 = api.trends_place(1) # from the end of your code
# trends1 is a list with only one element in it, which is a
# dict which we'll put in data.
data = trends1[0]
# grab the trends
trends = data['trends']
# grab the name from each trend
names = [trend['name'] for trend in trends]
# put all the names together with a ' ' separating them
# trendsName = ' '.join(names)
print(names)
