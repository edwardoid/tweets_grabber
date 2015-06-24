#!/usr/bin/python2

from config import Config
from database import *
from stream_listener import *
from twitter import Twitter

twi = Twitter()
twi.stream(StreamListener())

raw_input()
