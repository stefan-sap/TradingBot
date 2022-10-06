from alpaca.trading import *
from config import *

def get_account():
    trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
    account = trading_client.get_account()
    return trading_client

def create_order(symbol, qty, type, side, time_in_force):

    market_order = MarketOrderRequest(
        symbol = symbol,
        qty = qty,
        type = type,
        side = side,
        time_in_force = time_in_force
    )

    # for property_name, value in market_order:
    #     print(f"\"{property_name}\": {value}")

    return market_order

def submit_order(trading_client, symbol, qty, type, side, time_in_force):
    order = create_order(symbol, qty, type, side, time_in_force)
    print(order)
    trading_client.submit_order(order)

submit_order(get_account(), "BTC/USD", 1, "market", "buy", "gtc")
# get_account()

#Hi!



