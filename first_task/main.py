"""All main work is done right here.

For future: sns.scatterplot(x='Num ratings',y = 'Users', hue = 'Rank',data = df)
"""

import first_task.tent as tent
import first_task.ngrams as ngrams
import first_task.refinetable as rt
import pandas as pd
import nltk
import wordcloud
import matplotlib.pyplot as plt


def text_freq_plot(counter):
    """
    Plot image with frequency distribution of the most frequent words.

    The more often the word appears in the counter the bigger it depicted on the image.
    :param counter: Counter object
    """
    counter = dict(counter)
    pic = wordcloud.WordCloud(width=1600, height=800, colormap='viridis',
                              background_color='white').generate_from_frequencies(counter)
    plt.figure(figsize=(20, 10))
    plt.imshow(pic, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig('images/wordcloud4.png', bbox_inches='tight')
    plt.show()


def linear_freq_plot(counter):
    """Get frequency linear distribution"""
    freqlist = nltk.FreqDist(counter)
    plt.figure(figsize=(16, 5))
    freqlist.plot(60)


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


if __name__ == '__main__':
    # df = tent.parse_sitemap(find_theme=True,create_csv=True)
    df = pd.read_csv('extensions.csv')
    text = rt.con_bycolumn(df, 'Description')  # get all descriptions together
    ngr = ngrams.getNgrams(text, 2)
    print(ngr)
    ngr = del_n_comm(ngr)  # call any plotting function for this Counter object
    linear_freq_plot(dict(ngr))
    # text_freq_plot(ngr)
