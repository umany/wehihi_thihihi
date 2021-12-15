import configparser

from twitter import *

config = configparser.ConfigParser()
config.read("config.ini")
app_name = config["Twitter"]["AppName"]
consumer_key = config["Twitter"]["ConsumerKey"]
consumer_secret = config["Twitter"]["ConsumerSecret"]

oauth_dance(app_name, consumer_key, consumer_secret, "token", False)
