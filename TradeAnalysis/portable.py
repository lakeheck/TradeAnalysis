import pandas as pd
import numpy as np
from itertools import product
from scipy.stats import zscore

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


#inputs are data, list of asset combinations (taken from universe_selection.py), and start date for calcualtion
#function finds spread of each combination and calucaltes the spread's current level as a ratio of its proximity to the min and max 
#spread value over the time period specified. function then creates output by sorting combinations  by ratio, with the highest ratio first
#this will prioritize spreads that are at historically low levels and present good opportunity for wideners
def historical_spread_analysis(data, combinations, start_date):
    data = data.loc[start_date:]
    output=[]
    for bull, bear in combinations: 
        spread = data[bull] - data[bear]
        ratio = (max(spread)-spread[-1])/(spread[-1]-min(spread))
        output.append([[bull, bear], ratio])

    return sorted(output, key=lambda x: x[-1], reverse=True)


folder = 'C:\\Users\\lakeh\\Documents\\personal\\TradeAnalysis\\'
ticker_list = 'C:\\Users\\lakeh\\Documents\\personal\\TradeAnalysis\\ticker_master_list.csv'
data_file = folder + 'ticker_master_data.csv'


tickers = get_tickers(ticker_list)
data = pd.read_csv(data_file, index_col=0)

#the below would be syntax to run USD short dated front end vs all other country short dated front end
#bullish_tickers,bearish_tickers = select_securities(tickers, country='USD', front_back='front', short_long='short', inflation=False)

#setting up to run USD short dated front end vs AUD
bullish_tickers,_ = select_securities(tickers, country='USD', front_back='front', short_long='short', inflation=False)
bearish_tickers,_ = select_securities(tickers, country='USD', front_back='back', short_long='short', inflation=False)

asset_combos = generate_combinations([bullish_tickers, bearish_tickers])

#call optimization function
#this one returns sorted list
t = historical_spread_analysis(data, asset_combos)

for i in range(20):
    print(tickers[tickers['Ticker']==t[i][0][0]]['Des'].values, "/", tickers[tickers['Ticker']==t[i][0][1]]['Des'].values, ': ', t[i][-1])
