import tweepy
import pandas as pd

consumer_token = '8TkJOG3N27zpnPp5o7kEx9JR7'
consumer_secret = '92pHHeFBHYLaow67r2sBUXhBBj8piI2PKi1ji3dZxQ5b6LWGkH'
auth = tweepy.AppAuthHandler(consumer_token, consumer_secret)

api = tweepy.API(auth)

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

user_ids = []
tweet_id = []
num_likes = []
num_retwts = []
text = []
tweets = pd.DataFrame()
for i in users.id:
    for status in tweepy.Cursor(api.user_timeline, user_id = i).items(100):
        if (not status.retweeted) and ('RT @' not in status.text):
            user_ids.append(status._json['user']['id'])
            tweet_id.append(status._json['id'])
            text.append(status._json['text'])
            num_likes.append(status._json['favorite_count'])
            num_retwts.append(status._json['retweet_count'])
    temp = pd.DataFrame.from_records([user_ids, tweet_id, text, num_likes, num_retwts]).T
    temp.columns = ['user_id', 'tweet_id', 'text', 'num_likes', 'num_retwts']
    tweets = pd.concat([tweets, temp])

for user in list[1:len(list)]._json.values[4]:
    print(user)
list[2]._json.values()

tweepy.Cursor(api.user_timeline, user_id = user_ids[1]).items(100)

#Unique followers that aren't following all of us
#Like most of my followers are "for Amash" accounts", I'd love to know more about the ones who aren't and what attracted them
#Eric (Long Island for Amash)Today at 5:13 PM
#If you could somehow analyze overlap of followers between accounts
#If you can analyze location too
#Would be nice to know going forward how many of my followers are actually from Long Island
