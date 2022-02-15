import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import BaseCollector
# from GlobalNewsCollector import BaseCollector
import requests
from bs4 import BeautifulSoup
from datetime import date

class People(BaseCollector.BaseCollector):

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
        # Retrive information under title and extract date published
        date_source_info = soup.find('div', attrs={'class': 'col-1-1 fl'}).text.strip().split("|")
        articleInfo['date_published'] = date_source_info[0]
        articleInfo['date_retrieved'] = date.today().strftime("%d-%m-%Y")
        articleInfo['url'] = url

        # Handle missing author articles
        try:
            articleInfo['author'] = soup.find('div', attrs={'class':'author cf'}).text 
        except AttributeError:
            articleInfo['author'] = 'N/A'    
        articleInfo['title'] = soup.find('div', attrs={'class':'col col-1 fl'}).find('h1').text
        articleInfo['publisher'] = "Central Committee of the Chinese Communist Party"
        articleInfo['publisher_url'] = "http://www.people.com.cn" 

        # Extract article info:
        paragraph_table = soup.find('div', attrs={'class':'rm_txt_con cf'})
        body = ""
        # Paragraphs should not have classes
        for paragraph in paragraph_table.find_all('p'):
            try:
                ignore = paragraph['class']
            except KeyError:
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

p = People()
p.get_article("http://world.people.com.cn/n1/2022/0215/c1002-32352004.html")