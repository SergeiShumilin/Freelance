"""All main work is done right here."""
import wordcloud as wordcloud

import first_task.tent as tent
import first_task.ngrams as ngrams
import first_task.refinetable as rt
import pandas as pd
import nltk
from nltk.corpus import inaugural
import wordcloud
import matplotlib.pyplot as plt


def graph_freq_plot(counter):
    pic = wordcloud.WordCloud(max_font_size=60,colormap='magma',background_color='white').generate_from_frequencies(counter)
    plt.figure(figsize=(20,10))
    plt.imshow(pic,interpolation= 'bilinear')
    plt.axis('off')
    plt.show()


def freq_plot(counter):
    """Get frequency linear distribution"""
    freqlist = nltk.FreqDist(counter)
    plt.figure(figsize=(16,5))
    freqlist.plot(50)


if __name__ == '__main__':
    #df = tent.parse_sitemap(find_theme=True,create_csv=True)
    df = pd.read_csv('extensions.csv')
    text = rt.con_bycolumn(df,'Name') # get all descriptions together
    ngr =  ngrams.getNgrams(text,2)
    print(dict(ngr))
    graph_freq_plot(dict(ngr))
