from datastore import DataStore
from config import Config
import couchdb

class CouchDBStore(DataStore):

	__server = None
	__params_db = None
	__tweets_db = None

	def __init__(self):
		self.__server = couchdb.Server(Config.DB_PROT + Config.DB_HOST + ":" + Config.DB_PORT)
		self.__server.resource.credentials = (Config.DB_USER, Config.DB_PASS)
		self.__params_db = self.__server[Config.DB_PARAMS];
		self.__tweets_db = self.__server[Config.DB_TWEETS]

	def get_parameter(self, param_name):
		if self.__params_db is None:
			return None
		res = self.__params_db.view("parameters/value")[param_name]
		for r in res:
			return r.value
		return None

	def save(self, tweet):
		if self.__tweets_db is not None:
			self.__tweets_db.save(status._json)