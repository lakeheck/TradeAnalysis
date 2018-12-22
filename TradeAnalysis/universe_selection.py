import pandas as pd
import pdblp
import numpy as np
from itertools import product

folder = 'C:\\Users\\lakeh\\Documents\\personal\\TradeAnalysis\\'
ticker_list = 'C:\\Users\\lakeh\\Documents\\personal\\TradeAnalysis\\ticker_master_list.csv'

tickers = pd.read_csv(ticker_list)
usd_tickers=tickers[tickers['Country']=='USD']


#con = pdblp.BCon(debug=True, port=8194, timeout=5000)
#con.start()

# pulls tickers from csv file
def get_tickers(filepath):
    ticker_list = filepath
    return pd.read_csv(ticker_list)


#slice full tickers for the countries in question
#inputs bullish and bearish country, ticker list read into memory, other params
#params: List of keywords to restrict asset universe by e.g. ['inflation', 'CB pricing']
#returns: list of all combinations of assets for each country
## TODO: when added the direction value to each, take into account for creating combinations
#TODO: add logic for param selection
def generate_universe(bullish=None, bearish=None, tickers=None, params=None):
    bull_tickers = tickers[tickers['Country']==bullish]['Ticker'].values
    bear_tickers = tickers[tickers['Country']==bearish]['Ticker'].values
    return list(product(bull_tickers, bear_tickers))


