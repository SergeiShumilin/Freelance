"""
Parse the CS and retrieve data into a table.

Point `find_theme = True` in order to search extension containing theme ot Theme
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import re


def parse_sitemap(find_theme=False, create_csv = False):
    """
    Main here to parse the Chrome's sitemap

    :param find_theme:  bool if True searching for extension containing the word theme or Theme
    :param create_csv:  bool if True creates a .scv in the source folder with retrieved extensions
    :return: df with all found extensions
    """
    if find_theme:
        main_df = pd.DataFrame(np.array([[0, 0, 0, 0, 0, 0]]), columns=['Name', 'Users', 'Rank', 'Num ratings', 'Link',
                                                                        'Description'])
    else:
        main_df = pd.DataFrame(np.array([[0, 0, 0, 0, 0]]), columns=['Name', 'Users', 'Rank', 'Num ratings', 'Link'])

    page = requests.get('https://chrome.google.com/webstore/sitemap')
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        i = 601
        for url in list(soup.find_all('loc'))[601:701]:
            print('i = ' + str(i))
            df = extract_ext(url.text, find_theme)
            main_df = main_df.append(df, ignore_index=True)
            i += 1
    except Exception as e:
        print(e.__str__())
    finally:
        main_df = main_df.reset_index(drop=True)
        if create_csv:
            main_df.to_csv('extensions.csv')
        return main_df


def extract_ext(url, find_theme):
    if find_theme:
        interm_df = pd.DataFrame(np.array([[0, 0, 0, 0, 0, 0]]),
                                 columns=['Name', 'Users', 'Rank', 'Num ratings', 'Link',
                                          'Description'])
    else:
        interm_df = pd.DataFrame(np.array([[0, 0, 0, 0, 0]]), columns=['Name', 'Users', 'Rank', 'Num ratings', 'Link'])

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for url in soup.find_all('loc'):
        df = ext_info(url.text, find_theme)
        interm_df = interm_df.append(df, ignore_index=True)
    return interm_df


def ext_info(url, find_theme):
    """
    Extract info about particular extension

    Extracts four main features: name, number of users, number of comments, rank

    :param url: extension's web page
    :param find_theme: bool

    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = get_name(soup)
    return get_theme(name,soup,url)
"""    if find_theme:
        if bool(re.search(r'[Tt]heme', name)):
            return get_theme(name, soup, url)
    else:
        return get_ext(name, soup, url)"""



def get_ext(name, soup, url):
    rank = get_rank(soup)
    users = get_users(soup)
    ratings = get_ratings(soup)
    return pd.DataFrame([[name, users, rank, ratings, url]], columns=['Name', 'Users', 'Rank', 'Num ratings', 'Link'])


def get_theme(name, soup, url):
    rank = get_rank(soup)
    users = get_users(soup)
    ratings = get_ratings(soup)
    description = get_description(soup)
    print('+extns')
    return pd.DataFrame([[name, users, rank, ratings, url, description]],
                        columns=['Name', 'Users', 'Rank', 'Num ratings', 'Link', 'Description'])


def get_name(soup):
    name_tag = soup.find('h1', class_='e-f-w')  # gets the ext's name
    if name_tag is not None:
        name = name_tag.get_text()
        return name
    else:
        return ''


def get_users(soup):
    users = soup.find('span', class_='e-f-ih')  # gets the ext's users
    if users is not None:
        info = users['title']
        match = re.findall(r'(\d*)', info)
        return int(''.join(match))
    else:
        return 0


def get_rank(soup):
    rank_tags = soup.find('span', class_='q-N-nd')  # gets the ext's rank
    if rank_tags is not None:
        rank = rank_tags['aria-label']
        match = re.search(r'(\d\.\d)', rank)
        if match is not None:
            return float(match.group())
        elif rank == ' No user rated this item.':
            return 0
        else:
            return float(re.findall(r'(\d)\s', rank)[0])


def get_ratings(soup):
    ratings = soup.find('span', class_='q-N-nd')  # gets the ext's number of ratings
    if ratings is not None:
        return int(ratings.get_text()[1:-1])
    else:
        return 0


def get_description(soup):
    desc_tag = soup.find('pre', class_='C-b-p-j-Oa')  # gets the ext's desc
    short_desc = soup.find('div', class_='C-b-p-j-Pb')  # short description
    if (desc_tag is not None) & (short_desc is not No e):
        return short_desc.get_text() + desc_tag.get_text()
    elif desc_tag is not None:
        return desc_tag.get_text()
    elif short_desc is not None:
        return short_desc.get_text()
    else:
        return ''


parse_sitemap(create_csv=True,find_theme = True)