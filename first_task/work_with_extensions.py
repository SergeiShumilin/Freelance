


def refine_table(table, drop_Descr = False):
    import pandas as pd
    df = pd.read_csv(table, index_col=0)
    df = df.sort_values(['Users', 'Rank'], ascending=[False, False])
    df.dropna()
    df = df.reset_index(drop=True)
    if drop_Descr:
        df = df.drop(['Description'], axis=1)
    df.to_csv('themes.csv')

refine_table('extensions.csv')
