import pandas as pd
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt
sns.set_style("darkgrid")
plt.rcParams.update({'figure.max_open_warning': 0})

ticker_list = ["TSLA", "AAPL", "GS", "A", "SPY", "IVV"]
def get_data(ticker_list):
    for ticker in ticker_list:
        t = yf.Ticker(ticker)
        df = t.history(ticker_list, start="2022-01-01", end="2022-12-31", interval="1d")
        Close = df['Close']
        np.log(Close).to_csv("{}.csv".format(ticker))
        #and so on for each ticker --> csv file

get_data(ticker_list)