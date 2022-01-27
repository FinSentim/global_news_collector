from bs4 import BeautifulSoup
import requests
from abc import ABC, abstractmethod
# from GlobalNewsCollector.BaseCollector import BaseCollector
from datetime import date

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import BaseCollector

class yicai(BaseCollector.BaseCollector):

    def get_articles_list(self, url: str) -> list:

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')

        articles = soup.find('div', attrs={'id':'headlist'})
        article_list = []

        for article in articles.find_all('a', attrs={'class':'f-db'}, href=True):
            article_list.append(self.get_article('https://www.yicai.com'+article['href']))

        return article_list
    
    def get_article(self, url: str) -> dict:

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')

        date_retrieved = date.today().strftime("%d %b %Y")

        article_info = soup.find('div', attrs={'class':'title f-pr'})
        title = article_info.h1.text
        author = article_info.find('p', attrs={'class':'names'}).text[3:]
        date = article_info.em.text

        # text body currently doesn't filter away links and the like but can easily be modified for desired output format:
        text = soup.find('div', attrs={'id':'multi-text'}).text

        dictionary = {
            'date_published': date,
            'date_retrieved': date_retrieved,
            'url' : url,
            'title': title,
            'publisher': 'yicai',
            'publisher_url': 'https://www.yicai.com/',
            'author': author,
            'body': text
        }

        return dictionary

        



