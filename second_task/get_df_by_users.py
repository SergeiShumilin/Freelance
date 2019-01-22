import pandas as pd
import nltk

def get_df(down, upper, lang):
    """
    Sort the df by users number and by language.

    Saves df to dfs/.

    :param down: bottom border of users number
    :param upper: upper border of users number
    :param lang: sort by lang
    :return: sorted pandas df
    """
    df = pd.read_csv('../first_task/all_extensions.csv', index_col=0)
    df = df[(df['Users'] > down) & (df['Users'] < upper) & (df['Link'].str.contains('hl=' + lang))]
    df.to_csv('dfs/extension ' + str(down) + '_' + str(upper) + '.csv')
    return df


def tokenize(df):
    """
    Compile all description in a df into a single text. Make it tokenized.

    :param df: pandas df
    :return: tokenized text of descriptions in lower case
    """
    text = df['Description'].tolist()
    text = ' '.join(text)
    text = nltk.word_tokenize(text.lower())
    return [word for word in text if word.isalpha()]
