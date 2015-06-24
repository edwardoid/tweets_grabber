#!/usr/bin/python2

import tweepy
import twitter
import couchdb
import json
from config import *
from database import DB

class StreamListener(tweepy.streaming.StreamListener):
    """description of class"""
    def on_status(self, status):
        print ("Adding " + str(status.id))
        try:
            DB.save(status)
        except Exception as e:
            print("Exception: " + str(e));
            f = open("exception.log", "a");
            f.write("Exception: " + str(e) + "\n");
            f.close();
        except:
            print("Unknown error")
        
        return

    def on_error(self, status):
        print(status)
