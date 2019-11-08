import requests
from bs4 import BeautifulSoup

def crawl(target):
    response = requests.get(target)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    tags = soup.find_all('a')
    for tag in tags:
        print(tag.get('href'))