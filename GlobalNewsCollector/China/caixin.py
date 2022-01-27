import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from abc import ABC, ABCMeta, abstractmethod
import BaseCollector
import requests
from bs4 import BeautifulSoup
from datetime import date
# url to non-locked article https://www.caixinglobal.com/2022-01-26/cx-daily-major-evergrande-creditor-faces-wave-of-bad-loans-101834884.html
class caixin(BaseCollector.BaseCollector):

    # accepts a link to an article and returns a dictionary with the following keys: date_published: date 
    # of publication date_retrieved: date of retrieval url: url of the article title: title of the article 
    # publisher: Company or website that published the article publisher_url: url of the publisher 
    # author: author of the article body: text of the article
    def get_article(self, url: str) -> dict:

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        articleInfo = {}
        articleInfo['date_publised'] = soup.find('span', attrs={'class': 'bd_block', 'id':'pubtime_baidu'}).text
        articleInfo['date_retrieved'] = date.today().strftime("%d-%m-%Y")
        articleInfo['url'] = url
        articleInfo['author'] = soup.find('span', attrs={'class':'bd_block', 'id':'author_baidu'}).text        
        articleInfo['title'] = soup.find('title').text
        articleInfo['publisher'] = "Caixin Media"
        articleInfo['publisher_url'] = "https://www.caixin.com"
        
        print(articleInfo)
        return articleInfo
  
    # that accepts a link a page with multiple articles (for example business news page) and returns a 
    # list of dictionaries, where each dictionary is a result of calling get_article(url) on each article 
    # link.
    def get_articles_list(self, url: str) -> list: 
        pass

c = caixin()
# c.get_article("https://www.caixinglobal.com/2022-01-26/opinion-chinas-factories-are-still-indispensable-to-the-us-101835089.html")

