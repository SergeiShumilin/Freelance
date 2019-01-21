import csv
import pandas as pd
def concat():
    superdf = pd.read_csv("extensions.csv",index_col=0)
    df401 = pd.read_csv('extensions401_.csv',index_col=0)
    df830 = pd.read_csv('extensions830_.csv',index_col=0)
    df1600 = pd.read_csv('extensions1600_.csv',index_col=0)

    superdf = superdf.append(df401, ignore_index=True)
    superdf = superdf.append(df830, ignore_index=True)
    superdf = superdf.append(df1600, ignore_index=True)

    superdf = superdf.sort_values(['Users'],ascending=False)
    superdf.dropna()
    superdf = superdf.reset_index(drop=True)
    superdf.to_csv('all_extensions.csv')

df = pd.read_csv('all_extensions.csv',index_col=0,dtype={'Description':str})
#df.at[0,'Rank']=4
df.to_csv('all_extensions.csv', columns=['Name','Users','Rank','Num ratings','Link'],index=False)