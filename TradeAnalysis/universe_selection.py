import pandas as pd
import pdblp
import numpy as np
from itertools import product

folder = 'C:\\Users\\lakeh\\Documents\\personal\\TradeAnalysis\\'
ticker_list = 'C:\\Users\\lakeh\\Documents\\personal\\TradeAnalysis\\ticker_master_list.csv'

tickers = pd.read_csv(ticker_list)
usd_tickers=tickers[tickers['Country']=='USD']

data_file = folder + 'ticker_master_data.csv'
con = pdblp.BCon(debug=True, port=8194, timeout=5000)
con.start()

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


#slice full tickers based on param keyword inputs. tickers should be DF and params should be strings. inflation is boolean
# front_back takes one of ['front', 'back']. short_long takes one of ['short', 'long']
#return df of tickers satisfying the params, and list of complement tickers, that is the tickers from every other country satifsying the same params
def select_securities(tickers, country=None, front_back=None, short_long=None, inflation=False):
    assert country!=None
    assert len(tickers)>0

    country_tickers = tickers[(tickers['Country']==country) & (tickers['front_back']==front_back) & (tickers['short_long']==short_long) & (tickers['inflation']==inflation)]
    complement_tickers = tickers[(tickers['Country']!=country) & (tickers['front_back']==front_back) & (tickers['short_long']==short_long) & (tickers['inflation']==inflation)]

    return country_tickers, complement_tickers


#function to generate combinations of tickers for evaluation. if only one set of tickers is input, then we compare against 
#all other countries using same selection params. if there are two, we just run against each other 
#input is list of dataframes holding tickers in question generated from select_securities function
#for ease, we will say we buy the first, sell the second i.e. ticker_lists=[bullish tickers, bearish tickers]
def generate_combinations(ticker_lists):
    assert len(ticker_lists)>0
    return list(product(ticker_lists[0]['Ticker'].values, ticker_lists[1]['Ticker'].values))


