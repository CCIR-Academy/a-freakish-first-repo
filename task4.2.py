import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_client import SpotWebsocketClient as Client

import sqlite3
import json

config_logging(logging, logging.DEBUG)

messages = []

def message_handler(message):
    messages.append(message)
    


my_client = Client()
my_client.start()

my_client.agg_trade(
    symbol="btcusdt",
    id=1,
    callback=message_handler,
)

time.sleep(2)

# my_client.agg_trade(
#     symbol="bnbusdt",
#     id=2,
#     callback=message_handler,
# )

# time.sleep(60)

logging.debug("closing ws connection")
my_client.stop()

json_string = json.dumps(messages)

with open ('simpledatfile.json', 'w') as f:
    f.write(json_string)


