#!/usr/bin/python2

import json
class ConfigParser(dict):
    """Configuration"""

    def __init__(self, file_name):
        with open(file_name) as cfg_file:
            dict.__init__(self, json.load(cfg_file))


Config = ConfigParser("cfg.json")
