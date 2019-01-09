"""Work with DataFrames. Concatenating columns.

        main_df = main_df.drop([0, 1])
"""


def con_bycolumn(df, column):
    """
    Concatenate column's
    :param df:
    :param column: any column
    :return: one large string
    """

    df = df[df[column]!=0].dropna()
    return " ".join(df[column])

def drop_na_desc(table, drop_Descr = False):
    """
    Drop Nones and Descrition column
    :param table:
    :param drop_Descr:
    :return:
    """
    import pandas as pd
    df = pd.read_csv(table, index_col=0)
    df = df.sort_values(['Users', 'Rank'], ascending=[False, False])
    df.dropna()
    df = df.reset_index(drop=True)
    if drop_Descr:
        df = df.drop(['Description'], axis=1)
    df.to_csv('themes.csv')

import pandas as pd
main_df = pd.read_csv('extensions.csv')
main_df = main_df.drop([0, 1])
main_df.to_csv('extensions.csv')