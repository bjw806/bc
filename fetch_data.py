import numpy as np
import pandas as pd
import math
from datetime import datetime
from binance.client import Client
import sys

# Initialize the client
client = Client()


def fetchData(symbol, amount):
    # 1h = 3600000 ms
    #timeframe = '1h'
    #diff = 3600000
    timeframe = '1s'
    diff = 1000

    # Get current time, by getting the latest candle
    end = client.get_klines(symbol=symbol, interval=timeframe)[-1][0]

    # The list that keeps track of all the data before converting it to a DataFrame
    candleList = []
    print("\n\nFetching...")
    # Get the amount of data specified by amount parameter
    for x in range(amount):
        # Make the list from oldest to newest
        candleList = client.get_klines(symbol=symbol, interval=timeframe, endTime=end) + candleList
        t = str(x) + "/" + str(amount)
        sys.stdout.write("\r{0}".format(t))
        sys.stdout.flush()
        # Calculate the end point by using the difference in ms per candle
        end = end - diff * 500

    df = pd.DataFrame(candleList)

    # Only the columns containt the OHLCV data
    df.drop(columns=[6, 7, 8, 9, 10, 11], axis=1, inplace=True)
    df.columns = ["date", "open", "high", "low", "close", "volume"]

    # Convert time in ms to datetime
    df['date'] = pd.to_datetime(df['date'], unit='ms')

    # The default values are string, so convert these to numeric values
    df['open'] = pd.to_numeric(df['open'])
    df['high'] = pd.to_numeric(df['high'])
    df['low'] = pd.to_numeric(df['low'])
    df['close'] = pd.to_numeric(df['close'])
    df['volume'] = pd.to_numeric(df['volume'])

    # Volume in USDT
    df['volume'] = df.volume * df.close

    # Convert to csv file
    df.to_csv(r'./historical_data/history.csv', index=False)
    print("\rCSV Converted")

    return df
