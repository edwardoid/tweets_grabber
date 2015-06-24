#!/usr/bin/python2

from config import *
from couch import CouchDBStore

DB = None

if Config.DB_DRIVER is "couch":
	DB = CouchDBStore()