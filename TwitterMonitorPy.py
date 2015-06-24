#!/usr/bin/python2

import tweepy
from config import Config
from server import *
from stream_listener import *

filters = []
hts = parameter_value("hashtags")
kws = parameter_value("keywords")
if hts is not None:
    filters = hts
else:
    filters = []

if kws is not None:
    filters += kws

stream(filters)

raw_input()
