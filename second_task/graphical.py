"""
The module provides some graphical stuff needed to visualize the result of researching.
It generates linear and wordcloud formats.
"""

import matplotlib.pyplot as plt
import wordcloud
import nltk


def text_freq_plot(counter):
    """
    Plot image with frequency distribution of the most frequent words.

    The more often the word appears in the counter the bigger it depicted on the image.
    :param counter: Counter object
    """
    counter = dict(counter)
    pic = wordcloud.WordCloud(width=1600, height=800, colormap='magma',
                              background_color='white').generate_from_frequencies(counter)
    plt.figure(figsize=(20, 10))
    plt.imshow(pic, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig('images/CORAN_one_most_freq_minus200.png', bbox_inches='tight')
    plt.show()


def linear_freq_plot(counter):
    """Get frequency linear distribution"""
    freqlist = nltk.FreqDist(counter)
    plt.figure(figsize=(16, 5))
    freqlist.plot(60)
