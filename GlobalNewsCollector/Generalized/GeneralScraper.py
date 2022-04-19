from bs4 import BeautifulSoup
from readabilipy import simple_tree_from_html_string, simple_json_from_html_string
from lingua import LanguageDetectorBuilder
from langdetect import detect 
from datetime import datetime
import requests
# from GlobalNewsCollector.Generalized import LinkPatternMatch
# from GlobalNewsCollector.Generalized import Metadata


import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import BaseCollector
from Generalized.LinkPatternMatch import getlinks
import Generalized.Metadata




class GeneralScraper(BaseCollector.BaseCollector):

    def __init__(self) -> None:
        super().__init__()
        # instantiate the language detector, and decide on what languages it should be able to detect
        self.accepted_languages = ['HINDI', 'GERMAN', 'CHINESE']
        self.detector = LanguageDetectorBuilder.from_all_languages().build()

    def get_articles_list(self, url: str) -> list:
        """
        Scrap all articles visible in the "Latest news view".
        ---
        Args:
            url: The url of the website.
        Returns: A list containing a dictionary returned from get_article() for each article.
        """
        valid_links  = getlinks(url)
        articles = []
        for link in valid_links:
            dictionary = self.get_article(link)
            
            if dictionary != {}:
                articles.append(dictionary)
        
        return articles
        

        

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
        # fix encoding to handle different langauages
        r.encoding = r.apparent_encoding
        # Send response through readabilipy and get a parsable HTML tree
        tree = simple_tree_from_html_string(r.text)

        articleInfo = {}
        articleInfo = self.__extract_body_title(tree)
        
        articleInfo = self.__compare_article(articleInfo, r)

        #   Check if body probably is article and of a valid language
        print(self.__validate_article_body(articleInfo['body']))
        if self.__validate_article_body(articleInfo['body']) != True:
            return {}


        # Detect language, interperet lang as a string and extract language part
        lang = self.detector.detect_language_of(articleInfo['body'])
        articleInfo['Language'] = str(lang).split(".")[1]
        articleInfo['url'] = url
        articleInfo['date_retrieved'] = datetime.utcnow().strftime("%d-%m-%Y %H:%M")
        return articleInfo
        
    def __compare_article(self, articleInfo: dict, resp: requests.Response) -> dict:
        """
        Metod compares the scraped information from cleaned html tree with information returned from readabilipy library
        ---
        Args: \n
            articleInfo: Dictionary containging the scraped info from the clean HTML tree
            resp: response from http request
        Returns: \n
            An update dictionary that has compared scraped information from clean HTML tree with what readabilipy was able to scrap it self 
        """
        d = simple_json_from_html_string(resp.text, use_readability=True)
        text = ""

        for line in d['plain_text']:
            text = text + line['text']
        if len(text) > len(articleInfo['body']):
            articleInfo['body'] = text
        articleInfo['author'] = d['byline']
        # # Print test inorder to see difference
        # print(d['title'])
        # print(text)
        # print(d['byline'])
        # print("---------------BODY-------------------")
        # print(articleInfo['title'])
        # print(articleInfo['body'])
        return articleInfo


    def __validate_article_body(self, body: str) -> bool:

        """
        Method checks validity of article.
        Args: \n
            body: string of arcitle body. 
        Returns: \n
            A bool returning whether or not the article is sensible. Checking both length and language. 
            Accepted languages: GERMAN, HINDI, CHINESE 
        
        """
        validity = False

        # Ensure body is long enough
        print("body length: " + str(len(body)))
        if len(body) <= 100:
            return validity

        lang = self.detector.detect_language_of(body)
        # Extract the specific language name and check whether is is an accepted language or not
        if (str(lang).split('.')[1] in self.accepted_languages):
            validity = True
        return validity

    def __extract_body_title(self, tree) -> dict:
        """
        Method parses a html-tree for relevant infomration gatherd from the readabilipy library.
        ---
        Args: \n
            tree: a cleaned html tree that has been parsed by the readabilipy library
        Returns: \n
            returns a dictonary containing the found article body and found title
        """
        body, title = "", ""
        try:
            # Try to fetch the title
            for h1 in tree.find_all('h1'):
                title = h1.text

            if title == "":
                for h2 in tree.find_all('h2'):
                    title = h2.text
            # Get the article body
            for row in tree.findAll('p'):
                body = body + row.text

            # Create dictionary that contains body and title 
            return {'body':body, 'title':title}
        except AttributeError:
            return {}

        

    


gs = GeneralScraper()
# a = gs.get_article('https://hindi.business-standard.com/storypage.php?autono=186301')
a = gs.get_article('http://world.people.com.cn/n1/2022/0404/c1002-32391390.html')
# a = gs.get_article('http://finance.people.com.cn/n1/2022/0414/c1004-32398913.html')
# a = gs.get_article('https://www.manager-magazin.de/finanzen/bundesbank-praesident-joachim-nagel-glaubt-an-baldigen-zinsanstieg-a-58d5345b-db65-4262-ad46-4e447eb955a2')
# a = gs.get_article('https://www.theguardian.com/world/2022/apr/18/macron-lead-over-le-pen-stabilises-as-election-scrutiny-intensifies')
# print(a)
# for key in a.values():
#     print(key)
#     print(" ")


    
