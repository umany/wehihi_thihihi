from twitter import *

from bot_config import BotConfig
from madhom import shindan

config = BotConfig()
tw = Twitter(
    auth=OAuth(
        config.token, config.token_secret, config.consumer_key, config.consumer_secret
    ),
    retry=True,
)

tw.statuses.update(status=shindan())
