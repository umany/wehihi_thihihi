import configparser


class BotConfig:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.consumer_key = config["Twitter"]["ConsumerKey"]
        self.consumer_secret = config["Twitter"]["ConsumerSecret"]

        with open("token") as token_file:
            self.token = token_file.readline().strip()
            self.token_secret = token_file.readline().strip()
