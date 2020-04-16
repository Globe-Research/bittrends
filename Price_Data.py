from datetime import datetime
import pandas as pd
import numpy as np
import gzip
import requests
import json


def hist_data(exchange):

    # Input exchange to obtain price data from
    # Returns BTCUSD price data for Bitstamp, Kraken, Coinbase, CEX

    if exchange == 'Bitstamp':
        api = 'https://api.bitcoincharts.com/v1/csv/bitstampUSD.csv.gz'
    elif exchange == 'Kraken':
        api = 'https://api.bitcoincharts.com/v1/csv/krakenUSD.csv.gz'
    elif exchange == 'Coinbase':
        api = 'https://api.bitcoincharts.com/v1/csv/coinbaseUSD.csv.gz'
    elif exchange == 'CEX':
        api = 'https://api.bitcoincharts.com/v1/csv/cexUSD.csv.gz'
    else:
        return

    data = pd.read_csv(api,
                       compression='gzip',
                       error_bad_lines=False,
                       usecols=[0,1],
                       names=['Date','Price'])

    max_date = pd.DatetimeIndex([datetime(2019,12,13)]).astype(np.int64)//10**9
    max_date = int(max_date[0])

    price_data = data[data.Date <= max_date]
    price_data.Date = pd.to_datetime(price_data.Date,unit='s')
    price_data.set_index('Date',inplace=True)

    # Returns BTCUSD price data before 13/12/2019 as DataFrame

    return price_data


def Binance_data():

    # Timestamp for 17/08/2017 04:00:00 - earliest date for Binance exchange
    start = 1502942400000

    # Returns price data before 13/12/2019 as DataFrame
    end = pd.DatetimeIndex([datetime(2019,12,13)]).astype(np.int64)//10**6

    # 1 minute in milliseconds
    step = 60*1000

    start = start - step
    data = []
    binance = 'https://api.binance.com'
    kline = '/api/v3/klines'

    while start<end:
        start = start + step
        res = requests.get(binance + kline + '?symbol=BTCUSDT&limit=500&interval=30m&startTime=' + str(start))
        temp = json.loads(res.text)
        data.extend(temp)
        start = temp[-1][0]

        # Calls to API per minute limited
        time.sleep(1)

    # Obtains OHLC data for BTCUSDT, granularity = 30m
    # Can use finer granularity (1 minute) by changing to 'interval=1m' in res but much longer runtime

    price_data = pd.DataFrame(data).iloc[:, [4, 6]]
    price_data.columns = ['Price', 'Date']
    price_data.loc[:, 'Date'] = pd.to_datetime(price_data.loc[:, 'Date'], unit='ms')
    price_data.set_index('Date', inplace=True)

    return price_data


