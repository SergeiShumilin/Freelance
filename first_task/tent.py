from bs4 import BeautifulSoup
import requests

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

    Extracts four main features: name, number of users, number of references, rank

    :param url: extension's web page

    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib')
    name = soup.find('h1', class_='e-f-w').get_text()
    rank = soup.find('span', class_='q-N-nd')['aria-label']


    print(rank)
    print(name)




ext_info('https://chrome.google.com/webstore/detail/gauges-for-netatmo-weathe/pgdgaeigglghnbkloncmhelglgcinoph')