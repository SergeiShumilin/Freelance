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
        print(url.text)

def ext_info(url):
    pass


parse_sitemap()