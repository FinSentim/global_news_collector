from abc import ABCMeta
import requests
from bs4 import BeautifulSoup
from datetime import date



class managerMagazin(metaclass=ABCMeta):



        def get_article(self,url:str) -> dict:
                articleDict = {

                }
                r = requests.get(url)
                soup = BeautifulSoup(r.content,'html5lib')
                article = ""

                # finding the body of a specific article

                table = soup.find('div', attrs = {'class':'lg:mt-32 md:mt-32 sm:mt-24 md:mb-48 lg:mb-48 sm:mb-32'})
                if(table != None):
                        for row in table.findAll('div', attrs = {'class':'RichText RichText--iconLinks lg:w-8/12 md:w-10/12 lg:mx-auto md:mx-auto lg:px-24 md:px-24 sm:px-16 break-words word-wrap'}):
                                article = article + row.text

                # adding finishing paragraph to the body        
                table = soup.find('div', attrs={'class':'RichText RichText--iconLinks RichText--lastPmb0 RichText--lastInline lg:w-8/12 md:w-10/12 lg:mx-auto md:mx-auto lg:px-24 md:px-24 sm:px-16 break-words word-wrap'})
                if(table != None):
                        article = article + table.text

                #Remove unnecessary characters and whitespaces from string
                article = article.replace("\n","")
                article = article.replace("\"", "'")
                article = article.strip()

                

                # finding the author of an article
                author = soup.find('meta',attrs={"name":"author"}) 
                author = author["content"]

                # finding date published, alternatively use "last-modified" instead of "date"
                try:
                        datePublished = soup.find("meta",attrs={"name":"date"})
                        datePublished = datePublished["content"]
                        datePublished = datePublished[0:10]
                except:
                        pass
                
                # finding the title of the article
                title = soup.find("meta",property={"og:title"})
                title = title["content"]

                # getting todays date
                date_retrieved = date.today().strftime("%Y-%m-%d")
                
                #adding everything to a dictionary
                articleDict["date_published"] = datePublished
                articleDict["date_retrieved"] = date_retrieved
                articleDict["url"] = url
                articleDict["title"] = title
                articleDict["publisher"] = "manager magazin"
                articleDict["publisher_url"] = "https://www.manager-magazin.de/" 
                articleDict["author"] = author
                articleDict["body"] = article

                
                return articleDict
        

        def get_articles_list(self,url: str) -> list:
                
                article_list = []
                r = requests.get(url)
                soup = BeautifulSoup(r.content,'html5lib')

                # finds every article url on the page and calls for get_article with the fetched url and finally appends the retrieved dictionary to a list
                articles = soup.find('div',attrs={'class':'relative lg:pt-8 md:pt-8 sm:pt-4 lg:px-8 lg:bg-shade-lightest lg:dark:bg-black'})
                for row in articles.findAll('article',):
                        if("manager-magazin" in row.a["href"]):
                                dict = self.get_article(self,row.a["href"])
                                if(dict["body"] == ""):
                                        pass   
                                else:
                                        article_list.append(dict)

                return article_list

