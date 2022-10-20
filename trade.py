from alpaca.trading import *
from config import *
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.data.live import StockDataStream
from datetime import datetime, timedelta

hist_data = StockHistoricalDataClient(API_KEY, SECRET_KEY)
live_data = StockDataStream(API_KEY, SECRET_KEY)
api = TradingClient(API_KEY, SECRET_KEY, paper=True)


def getHistoricalData(ticker, daysback):
    endOfPeriod = datetime.now()
    startOfPeriod = (endOfPeriod - timedelta(days=daysback))

    parms = StockBarsRequest(
        symbol_or_symbols=["SPY"],
        timeframe=TimeFrame.Minute,
        start=str(startOfPeriod)[0:19],
        end=str(endOfPeriod)[0:19]
    )
    bars = hist_data.get_stock_bars(parms)
    return bars.df

def getMaxPrice(ticker, daysback):
    return getHistoricalData(ticker, daysback)["high"].max()


def compareCurrentToHistorical(current_price):
    if (live_data > getMaxPrice()):
        print("above 1")

async def bar_callback(bar):
    for property_name, value in bar:
        if (property_name == "close"):
            checkPrice(value)

# Subscribing to bar event
symbol = "SPY"
live_data.subscribe_bars(bar_callback, symbol)

live_data.run()

def main():
    # api.close_all_positions(cancel_orders=True)
    order = MarketOrderRequest(symbol="ETH/USD", qty=1, type=OrderType.MARKET, side=OrderSide.BUY, time_in_force=TimeInForce.GTC)

    # print(getHistoricalData("SPY", 4))
    print(getMaxPrice(ticker="SPY", daysback=4))
    # print(order)

    # api.submit_order(order)

    # print(get_position("BTC/USD"))
    # print(api.get_all_positions())
    # close_position("BTC/USD")

main()
