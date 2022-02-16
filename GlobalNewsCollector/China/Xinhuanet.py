from abc import ABCMeta
import requests
from bs4 import BeautifulSoup
from datetime import date, datetime, timezone

class Xinhuanet(metaclass=ABCMeta):

    def get_article(self,url:str) -> dict:
        article_dict = {

        }
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'html5lib')
        article = ""

        # finding the body of a specific article

        table = soup.find('div', attrs = {'id':'detail'})
        if(table != None):
                # for row in table.findAll('div', attrs = {'class':'probe_mc_important'}):
                for row in table.findAll('p'):
                        article = article + row.text
        
        

        # #Remove unnecessary characters and whitespaces from string
        article = article.replace("\n","")
        article = article.replace("\"", "'")
        article = article.replace("\u3000","")
        article = article.strip()
        
        try:    
                author = soup.find('meta',attrs={'property':'article:author'})
                author = author['content']
        except:
                # finding the editor of an article
                author = soup.find('span',attrs={"class":"editor"}) 
                author = author.text
                # formatting so we only retrieve the name
        
                author = author.split(":",1)[1]
                author = author.replace("】","")

        author = author.replace("\n","")


        # getiing date published for article
        date_published = soup.find('div',attrs={"class":"info"})
        date_published = date_published.text[0:20]
        date_published = date_published.replace("\n","")

        title = soup.find('title') 
        title = title.text.split("-",1)[0]
        title = title.replace("\n","")
        
        # # getting todays date
        date_retrieved = date.today().strftime("%Y-%m-%d") 
        
        #adding everything to a dictionary
        article_dict["date_published"] = date_published
        article_dict["date_retrieved"] = date_retrieved
        article_dict["url"] = url
        article_dict["title"] = title
        article_dict["publisher"] = "Xinhuanet"
        article_dict["publisher_url"] = "http://www.xinhuanet.com/" 
        article_dict["author"] = author
        article_dict["body"] = article

        return article_dict


    def get_articles_list(self,url: str) -> list:
            
        article_list = []
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'html5lib')

        articles = soup.find('body')
        for row in articles.findAll('div'):
                try:
                        if("http://www.news.cn" in row.a["href"]):
                                article_list.append(self.get_article(self,row.a["href"]))
                except:
                        pass
        

        return article_list




