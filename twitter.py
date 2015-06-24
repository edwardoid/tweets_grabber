#!/usr/bin/python2

from config import *
from tweepy import OAuthHandler

TwitteroAuthHandler = OAuthHandler(Config.TW_CONSUMER_KEY, Config.TW_CONSUMER_SECRET)
TwitteroAuthHandler.set_access_token(Config.TW_ACCESS_TOKEN, Config.TW_ACCESS_TOKEN_SECRET)
