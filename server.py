#!/usr/bin/python2

import couchdb
from config import *


Server = couchdb.Server(Config.DB_PROT + Config.DB_HOST + ":" + Config.DB_PORT)
Server.resource.credentials = (Config.DB_USER, Config.DB_PASS)

TweetsDatabase = Server[Config.DB_TWEETS]

#for d in TweetsDatabase:
#    if d[0] != '_':
#        TweetsDatabase.delete(TweetsDatabase[d])

def parameter_value(param):
    pvm = Server[Config.DB_PARAMS].view("parameters/value")
    res = Server[Config.DB_PARAMS].view("parameters/value")[param]
    for r in res:
        return r.value
    return None
