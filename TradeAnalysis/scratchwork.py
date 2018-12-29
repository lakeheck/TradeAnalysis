
#### to pull together the data dumps i got from bbg and make a dataframe
dirtyfiles=[folder+'datadump1.csv',folder+'datadump2.csv',folder+'datadump3.csv',folder+'datadump4.csv',
       folder+'datadump5.csv',folder+'datadump6.csv',folder+'datadump7.csv']
cleanfiles=[folder+'datadump1_cleaned.csv',folder+'datadump2_cleaned.csv',folder+'datadump3_cleaned.csv',folder+'datadump4_cleaned.csv',
       folder+'datadump5_cleaned.csv',folder+'datadump6_cleaned.csv',folder+'datadump7_cleaned.csv']


for i in range(len(dirtyfiles)):
    df=pd.read_csv(dirtyfiles[i], index_col=0).dropna(axis=1).to_csv(cleanfiles[i])


dfs=[]
for file in files:
    dfs.append(pd.read_csv(file, index_col=0))

df = pd.concat(dfs, axis=1, copy=False)
df = df.ix[:,~df.columns.duplicated()]
valid = tickers[tickers['Ticker'].isin(df.columns)]
valid.shape
valid.to_csv(ticker_list)


