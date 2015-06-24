#!/usr/bin/python2

from config import Config
from couch import CouchDBStore
from mongo import MongoDBStore

DB = None

if Config["database"]["driver"] == "couchdb":
	DB = CouchDBStore()
else:
	DB = MongoDBStore()