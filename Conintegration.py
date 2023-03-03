import pandas as pd
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr
import seaborn as sns
from datetime import datetime, timedelta, timezone
import matplotlib.pyplot as plt
from statsmodels.tsa.vector_ar.vecm import *
import random

class TestResult:
    integ = 0

def coint_test(x, y):
    x_data = np.array(pd.read_csv("{}.csv".format(x)).iloc[:, -1])
    y_data = np.array(pd.read_csv("{}.csv".format(y)).iloc[:, -1])
    arr = np.ndarray((len(x_data), 2))
    arr[:, 0] = x_data
    arr[:, 1] = y_data
    result = coint_johansen(arr, 0, 1)
    if np.all(result.trace_stat > result.trace_stat_crit_vals[:, 1]):
        if np.all(result.max_eig_stat > result.max_eig_stat_crit_vals[:, 1]):
            return True
    return False

print(coint_test("IVV", "SPY"))