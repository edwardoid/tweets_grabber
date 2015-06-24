#!/usr/bin/python2

from config import Config
import tweepy

class Twitter:
	__twitter_oAuth_handler = None
	__filter = ""
	def __init__(self):
		self.__twitter_oAuth_handler = tweepy.OAuthHandler(Config["twitter"]["consumer_key"], Config["twitter"]["consumer_secret"])
		self.__twitter_oAuth_handler.set_access_token(Config["twitter"]["access_token"], Config["twitter"]["access_token_secret"])
		self.__filter = []
		hts = Config["filter"]["hashtags"]
		kws = Config["filter"]["keywords"]
		if hts is not None:
			self.__filter = hts
		else:
			self.__filter = []

		if kws is not None:
			self.__filter += kws

	def stream(self, listener):
		stream = tweepy.Stream(self.__twitter_oAuth_handler, listener)
		stream.filter(track=self.__filter)

