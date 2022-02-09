#from lib2to3.pytree import Base
#from abc import ABC, abstractmethod
from GlobalNewsCollector import BaseCollector
from bs4 import BeautifulSoup
import requests
import datetime


class ChinaDailyScrapper(BaseCollector.BaseCollector):

    def get_article(self, url: str) -> dict:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        body = []
        author = None
        title = None
        dateOfPublish = None
        
        #Get body
        getBody = soup.findAll('div', attrs= {'id':'Content'})
        for row in getBody:
            for text in row.findAll('p'):
                body.append(text.text)
        
        #If empty page, skip this link
        if body == []:
            return

        #Get title
        getTitle = soup.findAll('h1', attrs= {'class':'dabiaoti'})
        if (getTitle == []):
            getTitle = soup.findAll('span', attrs= {'class':'main_title1'})
        if getTitle != []:
            title = getTitle[0].text

        #Get author and date of publish
        getArticleInfo = soup.findAll('div', attrs={'class':'xinf-le'})
        #temp list to split author and date
        splitTxt = []
        if getArticleInfo != []:
            splitTxt = getArticleInfo[0].text.split()
        #If no author is specified, splitTxt array will have a size < 1
        if len(splitTxt) > 1:
            author = splitTxt[1]
        if len(getArticleInfo) > 1:    
            dateOfPublish = getArticleInfo[1].text.removesuffix('\u3000')

     

        #dictionary to return
        article = {
            "body": body,
            "title":  title,
            "date_of_publication": dateOfPublish,
            "date_retrieved": datetime.datetime.now().strftime("%c"),
            "url": url,
            "author": author,
            "publisher": 'China Daily',
            "publisher_url": "https://cn.chinadaily.com.cn/"
            }
        return article

    def get_articles_list(self, url: str) -> list:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        links = []
        articles = []

        #Get left row of articles on Front page
        getLinksL = soup.findAll('div', attrs= {'class':'busBox1'})
        for row in getLinksL:
            for row2 in row.findAll('div', attrs = {'class':'mr10'}):
                links.append('https:' + row2.a['href'])


        #Get right row of articles on Front page
        getLinksR = soup.findAll('div', attrs= {'class':"yaowen"})
        for row in getLinksR:
            for row2 in row.findAll('li'):
                links.append('https:' + row2.a['href'])


        #Call get_article function with links collected in "links" list
        for link in links:
                articles.append(self.get_article(link))

        return articles 
    

#get_article("http://finance.chinadaily.com.cn/a/202201/25/WS61ef9ac6a3107be497a03cdf.html")    
#get_article("http://finance.chinadaily.com.cn/a/202201/25/WS61ef9ac6a3107be497a03cde.html")
#get_articles_list("https://cn.chinadaily.com.cn/")