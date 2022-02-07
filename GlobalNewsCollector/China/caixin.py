import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import BaseCollector
import requests
from bs4 import BeautifulSoup
from datetime import date

class caixin(BaseCollector.BaseCollector):

    def get_article(self, url: str) -> dict:
        """
        Scrap information from the article that is accessed with parameter url.
        ---
        Args:
            url: The url of the article to scrape.
        Returns: A dictionary containing:\n
                - Date published 
                - Date retrieved
                - Url
                - Author
                - Title
                - Publisher
                - Publisher url
        """
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        articleInfo = {}
        articleInfo['date_publised'] = soup.find('span', attrs={'class': 'bd_block', 'id':'pubtime_baidu'}).text
        articleInfo['date_retrieved'] = date.today().strftime("%d-%m-%Y")
        articleInfo['url'] = url

        # Handle missing author articles
        try:
            articleInfo['author'] = soup.find('span', attrs={'class':'bd_block', 'id':'author_baidu'}).text
        except AttributeError:
            articleInfo['author'] = 'N/A'    
        articleInfo['title'] = soup.find('div', attrs={'id':'conTit'}).find('h1').text.strip()
        articleInfo['publisher'] = "Caixin Media"
        articleInfo['publisher_url'] = "https://www.caixin.com"

        # Extract article info:
        paragraph_table = soup.find('div', attrs={'id':'Main_Content_Val'})
        body = ""
        for paragraph in paragraph_table.find_all('p'):
            body = body + paragraph.text.strip()
        
        articleInfo['body'] = body
        return articleInfo
  
    def get_articles_list(self, url: str) -> list:
        """
        Scrap all articles visible in the "Latest news view".
        ---
        Args:
            url: The url of the website.
        Returns: A list containing a dictionary returned from get_article() for each article.
        """

        r = requests.get(url) 
        soup = BeautifulSoup(r.content, 'html5lib')       
        articleList = []
        listOFArticles = soup.find('div', attrs={'class':'news_list'})
        for article in listOFArticles.find_all('dl'):
            par = article.find('p').find('a', href=True)['href']
            articleList.append(self.get_article(par))
        return articleList
