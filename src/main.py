import pandas as pd
import numpy as np
import json
from urllib.request import urlopen
from datetime import datetime
import matplotlib.pyplot as plt
import yfinance as yf
from api.algorithms import strategies as als


def plot( data , stockname):
    plt.style.use('fivethirtyeight')
    plt.figure(figsize=(12.5, 4.5))
    plt.plot(data[stockname], label=stockname, alpha=0.55, linewidth=1.0)
    plt.plot(data['SMA30'], label='SMA30',alpha=0.35, linewidth=1.5)
    plt.plot(data['SMA100'], label='SMA100',alpha=0.35, linewidth=1.5)
    plt.scatter(data.index, data['Buy_Signal_Price'], label='Buy', marker='^', color='green')
    plt.scatter(data.index, data['Sell_Signal_Price'], label='Sell', marker='v', color='red')
    plt.title(f'{stockname} Close Price History')
    plt.xlabel('')
    plt.ylabel('')
    plt.legend(loc='upper left')
    plt.show()

def getStock_Daily(name):
    api_key = '170JBDCXJPAQJXRK'
    request = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+name+'&apikey='+api_key
    response = urlopen(request)
    data = json.loads(response.read())
    df = pd.json_normalize(data['Time Series (Daily)'], ['4. close'])
    print(df)


def main():
    stockname = input("Type the stock name to search: ").upper()
    period = input("Insert the period to look for ():")
    ticket = als.Ticket(stockname)
    ticket.get_stock_history(period)
    if not ticket.hist.empty:
        #data = als.longterm_signal(hist, stockname)
        data = als.tma_strat(ticket)
        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(12.5, 4.5))
        plt.plot(data[ticket.name], label=ticket.name, alpha=0.55, linewidth=1.0)
        plt.plot(data['Short/Fast EMA'], label='Short/Fast EMA',alpha=0.35, linewidth=1.5)
        plt.plot(data['Middle/Medium EMA'], label='Middle/Medium EMA',alpha=0.35, linewidth=1.5)
        plt.plot(data['Long/Slow EMA'], label='Long/Slow EMA',alpha=0.35, linewidth=1.5)
        plt.scatter(data.index, data['Buy_Signal_Price'], label='Buy', marker='^', color='green')
        plt.scatter(data.index, data['Sell_Signal_Price'], label='Sell', marker='v', color='red')
        plt.xlabel('')
        plt.ylabel('')
        plt.legend(loc='upper left')
        plt.show()

if __name__ == '__main__':
    main()
    

