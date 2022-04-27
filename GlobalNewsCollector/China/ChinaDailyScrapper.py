from GlobalNewsCollector.BaseCollector import BaseCollector
from bs4 import BeautifulSoup
import requests
import datetime

class ChinaDailyScrapper(BaseCollector):

    def get_article(self, url: str) -> dict:
        """
        Scrapes information from an article from the website cn.chinadaily.com.cn/" accessed with the url parameter
        ---
        Args: \n
            url: the url of the article to scrape
        Returns: A dictionary containing: \n
                - Body
                - Title
                - Date of publication
                - Date retrieved
                - Url
                - Author
                - Publisher
                - Publisher url
        """
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
                body.append(text.text.replace(u'\xa0', u' '))
        
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
            "date_retrieved":  datetime.date.today().strftime("%Y-%m-%d"),
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

        #Call get_article function with links collected in "links" list and append it if it is a valid article (not null)
        for link in links:
                article = self.get_article(link)
                if article != None:
                    articles.append(article)

        return articles 
    