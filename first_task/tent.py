from bs4 import BeautifulSoup
import requests
import re
import scrapy

def parse_sitemap():
    page = requests.get('https://chrome.google.com/webstore/sitemap')
    soup = BeautifulSoup(page.content, 'xml')
    for url in soup.find_all('loc'):
        extract_ext(url.text)

def extract_ext(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'xml')
    for url in soup.find_all('loc'):
        ext_info(url.text)

def ext_info(url):
    """
    Extract info about particular extension

    Extracts four main features: name, number of users, number of comments, rank

    :param url: extension's web page

    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib')

    name = soup.find('h1', class_='e-f-w').get_text() #gets the ext's name

    rank = get_rank(soup.find('span', class_='q-N-nd')['aria-label']) #gets the ext's rank

    users = get_users(soup.find('span', class_='e-f-ih')['title']) #gets the ext's users

    reviews = get_reviews(url)

    print('Name: '+ name + '\nRank: ' + str(rank)+ '\nUsers: ' + str(users))

def get_users(info):
    match = re.findall(r'(\d*)', info)
    return int(''.join(match))

def get_reviews(url):
    pass














def get_rank(info):
    match = re.search(r'(\d\.\d)',info)
    return float(match.group())



ext_info('https://chrome.google.com/webstore/detail/evernote-web-clipper/pioclpoplcdbaefihamjohnefbikjilc')