from datastore import DataStore
from config import Config
import couchdb

class CouchDBStore(DataStore):

	__server = None
	__params_db = None
	__tweets_db = None

	def __init__(self):
		self.__server = couchdb.Server(Config["database"]["couchdb"]["protocol"] + Config["database"]["couchdb"]["host"] + ":" + str(Config["database"]["couchdb"]["port"]))
		self.__server.resource.credentials = (Config["database"]["couchdb"]["user"], Config["database"]["couchdb"]["password"])
		self.__tweets_db = self.__server[Config["database"]["couchdb"]["database"]]

	def save(self, tweet):
		if self.__tweets_db is not None:
			self.__tweets_db.save(tweet._json)