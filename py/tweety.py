import tweepy
import json
from datetime import datetime
configfile = 'C:\\Users\\Cooper\\Desktop\\TweetReed\\config\\config.json'

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
    api = auth()
    t = api.user_timeline(screen_name = handle, count = c, include_rts = False)
    #tweets = []
    tweets = {}
    index = 0
    for tweet in t:
        #tweets.append(tweet.text.encode('utf-8'))
        data = {
            "handle" : handle,
            "created_at" : tweet.created_at.timestamp(),
            "text" : tweet.text,
            "author" : tweet.author.name
        }
        tweets[index] = data
        index += 1
    return tweets


if __name__ == "__main__":
    out = get_tweets('realDonaldTrump', 3)
