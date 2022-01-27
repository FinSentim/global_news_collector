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

        articles = soup.find('div', attrs={'id':'headlist'}) # headlist contains the latest 25 articles
        article_list = []

        for article in articles.find_all('a', attrs={'class':'f-db'}, href=True):
            article_list.append(self.get_article('https://www.yicai.com'+article['href']))

        return article_list
    
    def get_article(self, url: str) -> dict:

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')

        date_retrieved = date.today().strftime("%d %b %Y") # current date, can be reformatted

        article_info = soup.find('div', attrs={'class':'title f-pr'}) # article header, used to extract multiple dictionary entries
        title = article_info.h1.text
        author = article_info.find('p', attrs={'class':'names'}).text[3:] # author formatted as '责编：' ('Responsible editor:') followed by the name
        date = article_info.em.text # time in UTC+8, probably

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