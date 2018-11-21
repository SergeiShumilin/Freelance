from bs4 import BeautifulSoup
import requests
import re

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

    reviews(url)

    print('Name: '+ name + '\nRank: ' + str(rank)+ '\nUsers: ' + str(users))

def get_users(info):
    match = re.findall(r'(\d*)', info)
    return int(''.join(match))

def reviews(url):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time

    driver = webdriver.Chrome()

    driver.get('https://chrome.google.com/webstore/detail/evernote-web-clipper/pioclpoplcdbaefihamjohnefbikjilc?hl=en')
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.ID, ':21'))).click()
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.h-z-Ba-ca.ga-dd-Va.g-aa-ca'))
    ).click()

    english = driver.find_element_by_xpath('//div[@class="ah-mg-j"]/span').text
    print('English: ' + english.split()[-1])

    wait.until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="g-aa-ca-ma-x-L" and text() = "All languages"]'))
    ).click()
    wait.until_not(EC.text_to_be_present_in_element((By.XPATH, '//div[@class="ah-mg-j"]/span'), english))
    time.sleep(2)

    AllCount = driver.find_element_by_xpath('//div[@class="ah-mg-j"]/span').text
    print('All languages: ' + AllCount.split()[-1])
    driver.close()


def get_rank(info):
    match = re.search(r'(\d\.\d)',info)
    return float(match.group())



ext_info('https://chrome.google.com/webstore/detail/evernote-web-clipper/pioclpoplcdbaefihamjohnefbikjilc')