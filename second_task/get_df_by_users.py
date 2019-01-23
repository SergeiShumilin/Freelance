"""
The module provides functions to work with Pandas dfs and nltk them.
"""

import pandas as pd
import nltk
from nltk import ngrams
from nltk.corpus import stopwords
from collections import Counter


def getdf(down, upper, lang):
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
    text = ' '.join(map(str, text))
    text = nltk.word_tokenize(text.lower())
    stopWords = set(stopwords.words('russian'))
    return [word for word in text if (word.isalpha()) and (word not in stopWords)]


def countwords(tokens):
    """
    Count occurrences of a word.

    :param tokens:
    :return: dict with ['word':number of inclusions]
    """
    count = Counter(tokens)
    return dict(count)


def getdict(down, upper, lang, ngram=False, n=2):
    """
    Return df with users form down to up and lang as language.

    :param n: number of grams
    :param ngram:
    :param down:
    :param upper:
    :param lang: any code eg 'en' or 'ru'
    :return: dict with frequency
    """
    if ngram:
        return countwords(ngrams(tokenize(getdf(down, upper, lang)),n))
    else:
        return countwords(tokenize(getdf(down, upper, lang)))


