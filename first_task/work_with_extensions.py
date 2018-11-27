import pandas as pd

df = pd.read_csv('extensions.csv',index_col=0)
df = df.sort_values(['Users','Rank'],ascending=[False,False])
df.dropna()
df = df.reset_index(drop=True)
df.to_csv('extensions.csv')