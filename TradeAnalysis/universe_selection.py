import pandas as pd
import pdblp
import numpy as np
from itertools import product

folder = 'C:\\Users\\lakeh\\Documents\\personal\\TradeAnalysis\\'
ticker_list = 'C:\\Users\\lakeh\\Documents\\personal\\TradeAnalysis\\ticker_master_list.csv'

tickers = pd.read_csv(ticker_list)
usd_tickers=tickers[tickers['Country']=='USD']

data_file = folder + 'ticker_master_data.csv'
#con = pdblp.BCon(debug=True, port=8194, timeout=5000)
#con.start()

# pulls tickers from csv file
def get_tickers(filepath):
    ticker_list = filepath
    return pd.read_csv(ticker_list)


#slice full tickers for the countries in question
#inputs bullish and bearish country, ticker list read into memory, data file path if needed, other params
#params: List of keywords to restrict asset universe by e.g. ['inflation', 'CB pricing']
#returns: price data for securites as dataframe, list of all combinations of assets for each country
## TODO: when added the direction value to each, take into account for creating combinations
#TODO: add logic for param selection
##TODO: API integration
def generate_universe(bullish=None, bearish=None, tickers=None, datafile=None, params=None):
    bull_tickers = tickers[tickers['Country']==bullish]['Ticker'].values
    bear_tickers = tickers[tickers['Country']==bearish]['Ticker'].values

    if not datafile==None:
        data = pd.read_csv(datafile, index_col=0)[np.append(bull_tickers,bear_tickers)]
    else:
        #this is where the logic for the api could be integrated
        pass

    return data, list(product(bull_tickers, bear_tickers))
