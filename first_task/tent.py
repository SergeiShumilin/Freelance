

def parse_ext2():
    from bs4 import BeautifulSoup
    import requests
    page = requests.get('https://chrome.google.com/webstore/sitemap')
    soup = BeautifulSoup(page.content, 'xml')
    titles = soup.find_all('sitemap')
    for title in titles:
        print(title.get_text())


parse_ext2()