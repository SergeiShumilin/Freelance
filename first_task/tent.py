from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import numpy as np


def parse_sitemap():
    main_df = pd.DataFrame(np.array([[0, 0, 0, 0, 0]]), columns=['Name', 'Users', 'Rank','Num ratings','Link'])

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


def ext_info(url):
    """
    Extract info about particular extension

    Extracts four main features: name, number of users, number of comments, rank

    :param url: extension's web page

    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib')

    name = get_name(soup)

    rank = get_rank(soup)

    users = get_users(soup)

    ratings = get_ratings(soup)


    print('Name: '+ name  + '\nRank: ' + str(rank)+ '\nUsers: ' + str(users)+'\nNum ratings: ' + str(ratings)+'\nLink: ' + url)
    return pd.DataFrame([[name, users, rank,ratings,url]], columns=['Name', 'Users', 'Rank','Num ratings','Link'])

def get_name(soup):
    name_tag = soup.find('h1', class_='e-f-w') #gets the ext's name
    if name_tag is not None:
        name = name_tag.get_text()
        return name
    else: return ''


def get_users(soup):
    users = soup.find('span', class_='e-f-ih') #gets the ext's users
    if users is not None:
        info = users['title']
        match = re.findall(r'(\d*)', info)
        return int(''.join(match))
    else: return 0

def get_rank(soup):
    rank_tags = soup.find('span', class_='q-N-nd')#gets the ext's rank
    if rank_tags is not None:
        rank = rank_tags['aria-label']
        match = re.search(r'(\d\.\d)',rank)
        if match is not None:
            return float(match.group())
        elif rank == ' No user rated this item.':
            return 0
        else:
            return float(re.findall(r'(\d)\s',rank)[0])

def get_ratings(soup):
    ratings = soup.find('span', class_='q-N-nd')  # gets the ext's number of ratings
    if ratings is not None:
        return int(ratings.get_text()[1:-1])
    else: return 0





parse_sitemap()


#ext_info('https://chrome.google.com/webstore/detail/evernote-web-clipper/pioclpoplcdbaefihamjohnefbikjilc?hl=en')
