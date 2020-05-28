import datetime
from  time import sleep
from binance.client import Client
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from scipy.fftpack import fft
from scipy.optimize import curve_fit
import re

time_syc = client.get_server_time()
time_syc=np.array(time_syc['serverTime'])
Symbol='ETHUSDT'
trades = client.get_recent_trades(symbol=Symbol)
trades=pd.DataFrame(trades)
trades.head()
trad=trades['price']
trad=trad.astype(np.float)
