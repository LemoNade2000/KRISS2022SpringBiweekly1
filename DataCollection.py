import pandas as pd
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt
import csv
sns.set_style("darkgrid")
plt.rcParams.update({'figure.max_open_warning': 0})


with open('TickerList.csv') as f:
    reader = csv.reader(f)
    ticker_list = list(reader)

print(ticker_list)

def get_data(ticker_list):
    for ticker in ticker_list:
        t = yf.Ticker(ticker)
        df = t.history(ticker_list, start="2020-01-01", end="2021-12-31", interval="1d")
        Close = df['Close']
        np.log(Close).to_csv("{}.csv".format(ticker))
        #and so on for each ticker --> csv file

get_data(ticker_list[0])