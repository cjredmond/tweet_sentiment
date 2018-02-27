import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from credentials.py import creds

class TwitterClient(object):

    def __init__(self):
        c = creds()
        consumer_key = c[0]
        consumer_secret_key = c[1]
        access_token = c[2]
        access_token_secret = c[3]

        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret_key)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
