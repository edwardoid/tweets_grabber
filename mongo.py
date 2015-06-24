from datastore import DataStore
from config import Config
from pymongo import MongoClient
import json

class MongoDBStore(DataStore):
	
	__client = None
	__database = None
	__tweets_collection = None

	def __init__(self):
		self.__client = MongoClient(Config["database"]["mongodb"]["host"], int(Config["database"]["mongodb"]["port"]));
		self.__database = self.__client.get_database(Config["database"]["mongodb"]["database"]);
		self.__tweets_collection = self.__database.get_collection(Config["database"]["mongodb"]["tweets_collection"])

	def save(self, tweet):
		self.__tweets_collection.insert(tweet._json)