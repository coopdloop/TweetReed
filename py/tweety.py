import tweepy
import json
from datetime import datetime
import os


configs = {
    "sam" : 'C:\\Users\\thecasual\\Desktop\\TweetReed\\config\\config.json',
    "cooper" : 'C:\\Users\\Cooper\\Desktop\\TweetReed\\config\\config.json',
    "server" : "testo"
}

for config in configs:
    if os.path.exists(configs[config]):
        configfile = configs[config]
        break

with open(configfile) as c:
   config = json.load(c)

consumer_key=config['consumerkey']
consumer_secret=config['consumersecret']
access_token=config['accesstokenkey']
access_token_secret=config['accesstokensecret']

def auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

def get_tweets(handle, c):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    t = api.user_timeline(screen_name = handle, count = c)
    tweets = {}
    index = 0
    for tweet in t:
        data = {
            "handle" : handle,
            "created_at" : tweet.created_at.timestamp(),
            "text" : tweet.text,
            "author" : tweet.author.name
        }
        tweets[index] = data
        index += 1
    return json.dumps(tweets)


if __name__ == "__main__":
    out = get_tweets('realDonaldTrump', 4)