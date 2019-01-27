"""
The module provides functions to work with Pandas dfs and nltk them.
"""

import pandas as pd
import nltk
from nltk import ngrams
from nltk.corpus import stopwords
from collections import Counter
from second_task import graphical as gr
import seaborn as sns
import matplotlib.pyplot as plt

def getdf(down, upper, lang=None):
    """
    Sort the df by users number and by language.

    Saves df to dfs/.
    TODO default - no language
    :param down: bottom border of users number
    :param upper: upper border of users number
    :param lang: sort by lang
    :return: sorted pandas df
    """
    down = down*1000
    upper = upper*1000
    df = pd.read_csv('../first_task/all_extensions.csv', index_col=0)
    if lang is not None:
        df = df[(df['Users'] > down) & (df['Users'] < upper) & (df['Link'].str.contains('hl=' + lang))]
    else:
        df = df[(df['Users'] > down) & (df['Users'] < upper)]
    print("df length: " + str(len(df)))
    df.to_csv('dfs/extension ' + str(down) + '_' + str(upper) + '.csv')
    sns.distplot(df['Users'], kde=False,color='#FB592D')
    plt.show()
    return df


def tokenize(df):
    """
    Compile all description in a df into a single text. Make it tokenized.

    :param df: pandas df
    :return: tokenized text of descriptions in lower case
    """
    text = df['Description'].tolist()
    print(text)
    number = len(df['Description'])
    text = ' '.join(map(str, text))
    text = nltk.word_tokenize(text.lower())
    stopWords = set(stopwords.words('english'))
    text = [word for word in text if (word.isalpha()) and (word not in stopWords)]
    length=len(text)
    print('Средняя длина строки: ' + str(length/number))
    return text


def countwords(tokens, k):
    """
    Count occurrences of a word.

    :param k: number of most common words to remove
    :param tokens:
    :return: dict with ['word':number of inclusions]
    """
    count = Counter(tokens)
    count = del_n_comm(count,del_n=k)
    return dict(count)


def getdict(down, upper, lang=None, ngram=False, n=2, del_comm=0):
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
        return countwords(ngrams(tokenize(getdf(down, upper, lang)),n), del_comm)
    else:
        return countwords(tokenize(getdf(down, upper, lang)), del_comm)


def del_n_comm(counter, del_n=0):
    """
    Delete n the most common words in the counter.
    :param counter: Counter object
    :param del_n: how many to delete
    :return: renewed counter
    """
    k = len(counter) - del_n
    counter = counter.most_common()[: -k - 1:-1]
    return counter


def gettextplot(down, upper, lang=None, n=2, ngram=False, del_comm=0):
    """
    Get word cloud.

    :param down:
    :param upper:
    :param lang:
    :param n:
    :param ngram:
    :param del_comm:
    :return:
    """
    gr.text_freq_plot(getdict(down, upper, lang, n=n, ngram=ngram, del_comm=del_comm), down, upper, lang)


def getlinearplot(down, upper, lang = None, n=2, ngram=False, del_comm=0):
    gr.linear_freq_plot(getdict(down, upper, lang, n=n, ngram=ngram, del_comm=del_comm), down, upper, lang)


#getlinearplot(30000,50000)
tokenize(getdf(5000,10000))
