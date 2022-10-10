"""
A calculator for indicators and other functionalities
Exists due to separation of concerns (other modules do not need to know how to calculate EMA/SMA)
"""

import talib
import numpy as np
import pandas as pd

def adx_series(high, low, close, n):
    return talib.ADX(high, low, close, timeperiod=n)

def ema_series(series, n):
    return talib.EMA(series, timeperiod=n)

def sma_series(series, n):
    return talib.SMA(series, timeperiod=n)