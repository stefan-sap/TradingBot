from alpaca.trading import *
from config import *

api = TradingClient(API_KEY, SECRET_KEY, paper=True)


# def is_position():
#     positions = api.get_all_positions()
#     if
#     pass

def get_position(symbol):
    positions = api.get_all_positions()
    position = positions[symbol]

    return position

    # qty = positions[symbol].qty

    # api.submit_order(symbol=symbol, qty=value, type="market", side="sell", time_in_force="gtc")


def main():
    # api.close_all_positions(cancel_orders=True)
    order = MarketOrderRequest(symbol="ETH/USD", qty=1, type=OrderType.MARKET, side=OrderSide.BUY, time_in_force=TimeInForce.GTC)

    # print(order)

    api.submit_order(order)

    # print(get_position("BTC/USD"))
    print(api.get_all_positions())
    # close_position("BTC/USD")

main()
