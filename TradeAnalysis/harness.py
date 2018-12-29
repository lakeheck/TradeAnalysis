from universe_selection import *
from optimization_functions import *
from matplotlib import pyplot as plt

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

for i in range(100):
    print(tickers[tickers['Ticker']==t[i][0][0]]['Des'].values, "/", tickers[tickers['Ticker']==t[i][0][1]]['Des'].values, ': ', t[i][-1])

