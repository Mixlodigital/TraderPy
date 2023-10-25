"""
    API Documentation
    https://bybit-exchange.github.io/docs/linear/#t-introduction
"""

# API Imports
from pybit import HTTP

# CONFIG VARIABLES
mode = "production"
ticker_1 = "BTCUSDT"
ticker_2 = "ETHUSDT"
signal_positive_ticker = ticker_2
signal_negative_ticker = ticker_1
rounding_ticker_1 = 2
rounding_ticker_2 = 3
quantity_rounding_ticker_1 = 3
quantity_rounding_ticker_2 = 2

limit_order_basis = True # will ensure positions (except for Close) will be placed on limit basis

tradeable_capital_usdt = 100 # total tradeable capital to be split between both pairs
stop_loss_fail_safe = 0.015 # stop loss at market order in case of drastic event
signal_trigger_thresh = 0.02 # z-score threshold which determines trade (must be above zero)

timeframe = 60 # make sure matches your strategy
kline_limit = 200 # make sure matches your strategy
z_score_window = 21 # make sure matches your strategy

# LIVE API
api_key_mainnet = "KT7vYOMXTsD3LKOW4o"
api_secret_mainnet = "Eex9sWcrIuE8wCftWrz0AbZIqKyoLqnkmOq1"

# TEST API
api_key_testnet = ""
api_secret_testnet = ""

# SELECTED API
api_key = api_key_testnet if mode == "test" else api_key_mainnet
api_secret = api_secret_testnet if mode == "test" else api_secret_mainnet

# SELECTED URL
api_url = "https://api-testnet.bybit.com" if mode == "test" else "https://api.bybit.com"
# ws_public_url = "wss://stream-testnet.bybit.com/realtime_public" if mode == "test" else "wss://stream.bybit.com/realtime_public"

# SESSION Activation
session_public = HTTP(api_url)
session_private = HTTP(api_url, api_key=api_key, api_secret=api_secret)
