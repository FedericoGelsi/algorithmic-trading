import pandas as pd
import numpy as np

def longterm_signal(ticket, stockname):
    SMA30 = pd.DataFrame()
    SMA30['Close'] = ticket['Close'].rolling(window=30).mean()
    SMA100 = pd.DataFrame()
    SMA100['Close'] = ticket['Close'].rolling(window=100).mean()
    data = pd.DataFrame()
    data[stockname] = ticket['Close']
    data['SMA30'] = SMA30['Close']
    data['SMA100'] = SMA100['Close']
    buy_sell_data = buy_sell(data, stockname)
    data['Buy_Signal_Price'] = buy_sell_data[0]
    data['Sell_Signal_Price'] = buy_sell_data[1]
    return data
    


def buy_sell(data, stockname):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1
    for i in range(len(data)):
        if data['SMA30'][i] > data['SMA100'][i]:
            if flag != 1:
                sigPriceBuy.append(data[stockname][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
            
        elif data['SMA30'][i] < data['SMA100'][i]:
            if flag != 0:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(data[stockname][i])
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)

    return (sigPriceBuy, sigPriceSell)

