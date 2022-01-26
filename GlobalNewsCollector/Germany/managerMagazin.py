from abc import ABCMeta
import requests
from bs4 import BeautifulSoup
from datetime import date

class managerMagazin(metaclass=ABCMeta):

        # def __init__(self):     
        #         pass   


        def get_article(self,url:str) -> dict:
                articleDict = {

                }
                r = requests.get(url)
                soup = BeautifulSoup(r.content,'html5lib')
                article = ""
                table = soup.find('div', attrs = {'class':'lg:mt-32 md:mt-32 sm:mt-24 md:mb-48 lg:mb-48 sm:mb-32'})
                if(table != None):
                        for row in table.findAll('div', attrs = {'class':'RichText RichText--iconLinks lg:w-8/12 md:w-10/12 lg:mx-auto md:mx-auto lg:px-24 md:px-24 sm:px-16 break-words word-wrap'}):
                                article = article + row.text
                        
                table = soup.find('div', attrs={'class':'RichText RichText--iconLinks RichText--lastPmb0 RichText--lastInline lg:w-8/12 md:w-10/12 lg:mx-auto md:mx-auto lg:px-24 md:px-24 sm:px-16 break-words word-wrap'})
                if(table != None):
                        article = article + table.text
                

                author = soup.find('meta',attrs={"name":"author"}) 
                author = author["content"]
                try:
                        datePublished = soup.find("meta",attrs={"name":"date"})
                        datePublished = datePublished["content"]
                except:
                        print("This URL sucks " + url)
                title = soup.find("meta",property={"og:title"})
                title = title["content"]

                date_retrieved = date.today().strftime("%d %b %Y")
                
                articleDict["date_published"] = datePublished
                articleDict["date_retrieved"] = date_retrieved
                articleDict["url"] = url
                articleDict["title"] = title
                articleDict["publisher"] = "Manager Magazin"
                articleDict["publisher_url"] = "https://www.manager-magazin.de/" 
                articleDict["author"] = author
                articleDict["body"] = article

                
                return articleDict
        

        def get_articles_list(self,url: str) -> list:
                badLink = "https://www.manager-magazin.de/harvard/"
                article_list = []
                r = requests.get(url)
                soup = BeautifulSoup(r.content,'html5lib')
                articles = soup.find('div',attrs={'class':'relative lg:pt-8 md:pt-8 sm:pt-4 lg:px-8 lg:bg-shade-lightest lg:dark:bg-black'})
                for row in articles.findAll('article',):
                        if("manager-magazin" in row.a["href"] and row.a["href"] != badLink):       
                                article_list.append(self.get_article(row.a["href"]))

                return article_list

# obj = managerMagazin()
# URL = "https://www.manager-magazin.de/"
# list = obj.get_articles_list(URL)      
# for i in list:
#         print(i)
#         print("\n")