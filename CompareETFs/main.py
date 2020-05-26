# Main program to download ETF data from Yahoo Finance and post process
# Data is downloaded from yahoo finance manually (There is no stable API unfortunately)

import glob, os
import pandas as pd
#plt.use('Agg')
from datetime import datetime
import seaborn as sns
import re

sns.set()


sourceFolder = 'Data'
files = glob.glob(os.path.join(sourceFolder,"*.csv"))

startDate = "2020-07-20"
endDate = "2020-05-19"

tickers = ['^IXIC','HACK','PRNT']

dfs= {}
for ticker in tickers:
    file = [file for file in files if ticker in file]
    dfs[ticker] = pd.read_csv(file[0])
#    dfs[ticker].index = dfs[ticker].Date
    dfs[ticker].index = pd.to_datetime(dfs[ticker].Date, format='%Y-%m-%d')
    
#df.Close.plot()





