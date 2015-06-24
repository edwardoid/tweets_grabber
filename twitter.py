#!/usr/bin/python2

from config import *
from database import DB
from tweepy import OAuthHandler

class Twitter:
	__twitter_oAuth_handler = None
	__filter = ""
	def __init__(self):
		self.__twitter_oAuth_handler = OAuthHandler(Config.TW_CONSUMER_KEY, Config.TW_CONSUMER_SECRET)
		self.__twitter_oAuth_handler.set_access_token(Config.TW_ACCESS_TOKEN, Config.TW_ACCESS_TOKEN_SECRET)
		self.__filter = []
		hts = DB.get_parameter("hashtags")
		kws = DB.get_parameter("keywords")
		if hts is not None:
			self.__filter = hts
		else:
			self.__filter = []

		if kws is not None:
			self.__filter += kws

	def stream(self, listener):
		stream = tweepy.Stream(self.__twitter_oAuth_handler, listener)
		stream.filter(track=self.__filter)

		