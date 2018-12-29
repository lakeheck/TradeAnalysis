import numpy as np
import pandas as pd
from scipy.stats import zscore


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