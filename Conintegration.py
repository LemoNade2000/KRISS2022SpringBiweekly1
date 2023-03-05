import pandas as pd
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr
import seaborn as sns
from datetime import datetime, timedelta, timezone
import matplotlib.pyplot as plt
from statsmodels.tsa.vector_ar.vecm import *
import random
import csv
import os

cd = os.getcwd()
class TestResult:
    integ = 0

def coint_test(x, y):
    x_data = np.array(pd.read_csv((cd + "/Data/{}.csv").format(x)).iloc[:, -1])
    y_data = np.array(pd.read_csv((cd + "/Data/{}.csv").format(y)).iloc[:, -1])
    arr = np.ndarray((len(x_data), 2))
    arr[:, 0] = x_data
    arr[:, 1] = y_data
    result = coint_johansen(arr, 0, 1)
    if np.all(result.trace_stat > result.trace_stat_crit_vals[:, 1]):
        if np.all(result.max_eig_stat > result.max_eig_stat_crit_vals[:, 1]):
            return True
    return False

#print(coint_test("IVV", "SPY"))

ticker_list = []
with open('TickerList.csv') as f:
    reader = csv.reader(f)
    ticker_list = list(reader)

ticker_list = ticker_list[0]
cointMatrix = pd.DataFrame(index = ticker_list, columns = ticker_list)

for ticker in ticker_list:
    x_data = np.array(pd.read_csv((cd + "/Data/{}.csv").format(ticker)).iloc[:, -1])
    if len(x_data) != 251:
        print(ticker)
pairs = []
for i in range(len(ticker_list)):
    print(i)
    for j in range(i, len(ticker_list)):
        if i == j:
            cointMatrix[ticker_list[i]][ticker_list[j]] = True
        else:
            cointMatrix[ticker_list[i]][ticker_list[j]] = coint_test(ticker_list[i], ticker_list[j])
            cointMatrix[ticker_list[j]][ticker_list[i]] = cointMatrix[ticker_list[i]][ticker_list[j]]
            if cointMatrix[ticker_list[i]][ticker_list[j]] == True:
                pairs.append((ticker_list[i], ticker_list[j]))

p = pd.DataFrame(pairs)
p.to_csv("Pairs.csv")

print(cointMatrix)
fig, axis = plt.subplots()
sns.heatmap(cointMatrix.astype(float), annot = False, ax = axis, cmap = "Blues")
fig.savefig("Heatmap.png")
