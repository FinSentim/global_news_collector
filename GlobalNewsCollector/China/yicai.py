from bs4 import BeautifulSoup
import requests
from abc import ABC, abstractmethod
from GlobalNewsCollector.BaseCollector import BaseCollector

class yicai(BaseCollector):


    def get_articles_list(self, url: str) -> list:
        article_list = []

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')

        # texts = soup.find('div', attrs={'class':'m-content m-scrollcontent m-content-4'})
        articles = soup.find('div', attrs={'id':'headlist'})

        for article in articles.find_all('a', attrs={'class':'f-db'}, href=True):
            article_list.append(self.get_article('https://www.yicai.com/'+article['href']))
            

        return article_list
    
    def get_article(self, url: str) -> dict:

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')

