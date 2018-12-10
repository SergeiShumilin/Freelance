"""Retrieve themes from all extensions"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np


def get_themes():
    main_df = pd.DataFrame(np.array([[0, 0, 0, 0, 0]]), columns=['Name', 'Users', 'Rank','Num ratings',
                                                                 'Link','Description'])
    page = requests.get('https://chrome.google.com/webstore/sitemap')
    soup = BeautifulSoup(page.content, 'xml')
    i = 0
    for url in soup.find_all('loc'):
        if i==50: break
        df = extract_ext(url.text)
        main_df = main_df.append(df, ignore_index=True)
        i+=1

    main_df = main_df.drop([0,1])
    main_df = main_df.reset_index(drop=True)
    main_df.to_csv('extensions.csv')

def extract_ext(url):
    interm_df = pd.DataFrame(np.array([[0, 0, 0, 0, 0]]), columns=['Name', 'Users', 'Rank','Num ratings','Link'])

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'xml')
    i = 0
    for url in soup.find_all('loc'):
        if i == 100000: break
        df = ext_info(url.text)
        interm_df = interm_df.append(df,ignore_index=True)
        i+=1
    return interm_df