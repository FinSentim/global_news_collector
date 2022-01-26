# import sys
# sys.path.append("../GlobalNewsCollector")
# from GlobalNewsCollector.BaseCollector import BaseCollector
from abc import ABC, ABCMeta, abstractmethod
# import `..\BaseCollector`
# from GlobalNewsCollector.BaseCollector import BaseCollector
#from abc import ABCMeta
#import GlobalNewsCollector.BaseCollector as A
import requests
from bs4 import BeautifulSoup

# url to non-locked article https://www.caixinglobal.com/2022-01-26/cx-daily-major-evergrande-creditor-faces-wave-of-bad-loans-101834884.html
class caixin(metaclass = ABCMeta):

    # accepts a link to an article and returns a dictionary with the following keys: date_published: date 
    # of publication date_retrieved: date of retrieval url: url of the article title: title of the article 
    # publisher: Company or website that published the article publisher_url: url of the publisher 
    # author: author of the article body: text of the article
    def get_article(self, url: str) -> dict:

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        body_table = soup.find_all('div', attrs={'id':'appContent'})
        for paragraph in body_table:
            for test in paragraph.find_all("p"):
                if (test.style==None):
                    print(test.text)
        #print(body_table.text)
        articleInfo = {"hej": "hejdå"}
        #     "date_published": "Ford",
        #     "date_retrieved": "Mustang",
        #     "url": url
        #     "title": 
        #     "publisher":
        #     "publisher_url":
        #     "author":
        #     "body":
        # }
      
        return articleInfo
  
    # that accepts a link a page with multiple articles (for example business news page) and returns a 
    # list of dictionaries, where each dictionary is a result of calling get_article(url) on each article 
    # link.
    def get_articles_list(self, url: str) -> list: 
        pass

c = caixin()
c.get_article("https://www.caixinglobal.com/2022-01-26/opinion-chinas-factories-are-still-indispensable-to-the-us-101835089.html")