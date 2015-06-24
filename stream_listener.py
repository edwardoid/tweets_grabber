#!/usr/bin/python2

import tweepy
import twitter
import couchdb
import json
from config import *
from server import *

class StreamListener(tweepy.streaming.StreamListener):
    """description of class"""
    def on_status(self, status):
        print ("Adding " + str(status.id))
        try:
            TweetsDatabase.save(status._json)
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



Stream = None
        
def stream(query):
    Stream = StreamListener()
    stream = tweepy.Stream(twitter.TwitteroAuthHandler, Stream)
    stream.filter(track=query)
#    stream.filter(track=query, languages = Config.TW_LANGUAGES)
