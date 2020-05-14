import tweepy
import pandas as pd

consumer_token = '8TkJOG3N27zpnPp5o7kEx9JR7'
consumer_secret = '92pHHeFBHYLaow67r2sBUXhBBj8piI2PKi1ji3dZxQ5b6LWGkH'
auth = tweepy.AppAuthHandler(consumer_token, consumer_secret)

api = tweepy.API(auth)
for list in tweepy.Cursor(api.get_list, list_id='1257345016705490944').items(10):
    print(list.id)


tweepy.Cursor(api.get_list, list_id='1257345016705490944')

list = api.list_members(list_id='1257345016705490944')

# Get User Names, IDs, Follower Counts
user_ids = []
user_names = []
followers = []
tweets = []
for user in tweepy.Cursor(api.list_members, list_id = '1257345016705490944').items(100):
    user_names.append(user._json['screen_name'])
    user_ids.append(user._json['id'])
    followers.append(user._json['followers_count'])
    tweets.append(user._json['statuses_count'])

users = pd.DataFrame.from_records([user_names, user_ids, followers, tweets]).T
users.columns = ['username', 'id', 'followers', 'tweets']
users = users.sort_values(by = 'followers', ascending = False)

num_likes = []
num_retwts = []
for status in tweepy.Cursor(api.user_timeline, user_id = user_ids[1]).items(100):
    num_likes.append(status._json[''])

for user in list[1:len(list)]._json.values[4]:
    print(user)
list[2]._json.values()

