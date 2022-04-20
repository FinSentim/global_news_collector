from bs4 import BeautifulSoup
from readabilipy import simple_tree_from_html_string, simple_json_from_html_string
from lingua import LanguageDetectorBuilder
from datetime import datetime
import requests
import re
from GlobalNewsCollector.Generalized.LinkPatternMatch import getlinks
from GlobalNewsCollector.Generalized.Metadata import get_metadata


# import os
# import sys
# sys.path.insert(1, os.path.join(sys.path[0], '..'))
# import BaseCollector
# from Generalized.LinkPatternMatch import getlinks
# from Generalized.Metadata import get_metadata




class GeneralScraper(BaseCollector.BaseCollector):

    def __init__(self) -> None:
        """
        Constructors that initiates tha languages detector, later used to validate the articel 
        """
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
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
            r = requests.get(url, headers = headers, timeout=5)    
            # fix encoding to handle different langauages
            r.encoding = r.apparent_encoding

            # if timeout kicked in, the respones will be none and then the function call should end
            if r == None:
                return {}
        except Exception:
            return {}
        # Send response through readabilipy and get a parsable HTML tree
        tree = simple_tree_from_html_string(r.text)

        articleInfo = {}
        articleInfo = self.__extract_metadata(url, r)
        articleInfo = self.__extract_body_title(tree, articleInfo)
        
        # add language of article text,
        
        lang = self.detector.detect_language_of(articleInfo['body'])
        articleInfo['language'] = str(lang).split(".")[1] if lang != None else ""

        articleInfo = self.__compare_article(articleInfo, r)

        #   Check if body probably is article and of a valid language
        if self.__validate_article_body(articleInfo['body']) != True:
            return {}


        # Detect language, interperet lang as a string and extract language part
        
        articleInfo['url'] = url
        articleInfo['date_retrieved'] = datetime.utcnow().strftime("%d-%m-%Y %H:%M")
        
        return articleInfo

    def __extract_metadata(self, url: str, r: requests.Response) -> dict:
        """
        Creates a dictionary and utilizes the functionality of metadata.py inorder to get the articles metadata if it exits
        ---
        Args:
            url: the article url
            r: the response from the http request
        Returns:
            A dictionary containing the infromation found from the metadata\n
            - title
            - author
            - date published
        """

        soup = BeautifulSoup(r.content, 'html.parser')
        articleInfo = get_metadata(url, soup)

        # Cange all none elements in dict to just be empty strings
        for k,v in articleInfo.items():
            if v is None:
                articleInfo[k] = ""

        # add url and date retrived
        articleInfo['url'] = url
        articleInfo['date_retrieved'] = datetime.utcnow().strftime("%d-%m-%Y %H:%M")
        
        # Check to ensure normal characters
        if self.__check_characters_in_string(articleInfo['author']):
            articleInfo['author'] = ""
        return articleInfo
        
    def __check_characters_in_string(self, s: str)->bool:
        """
        Returns true if a string contains digits or special characters.
        """
        return bool(re.match('.*\d+.*',s)) or bool(re.match('.*\W+.*',s))         

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
        
        try:
            d = simple_json_from_html_string(resp.text, use_readability=True)
            text = ""
            for line in d['plain_text']:
                text = text + line['text']
            if len(text) > len(articleInfo['body']):
                articleInfo['body'] = text
            if articleInfo['author'] == "" and not(self.__check_characters_in_string(d['byline'])):
                articleInfo['author'] = d['byline']
            # # Print test inorder to see difference
            # print(d['title'])
            # print(text)
            # print(d['byline'])
            # print("---------------BODY-------------------")
            # print(articleInfo['title'])
            # print(articleInfo['body'])
            return articleInfo
        except Exception:
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
        # print("body length: " + str(len(body)))
        if len(body) <= 100:
            return validity

        lang = self.detector.detect_language_of(body)
        # Extract the specific language name and check whether is is an accepted language or not
        if (str(lang).split('.')[1] in self.accepted_languages):
            validity = True
        return validity

    def __extract_body_title(self, tree, articleInfo: dict) -> dict:
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
            articleInfo['body'] = body
            if articleInfo['title'] == "":
                articleInfo['title'] = title
            # Create dictionary that contains body and title 
            return articleInfo
        except AttributeError:
            articleInfo['body'] = body
            return articleInfo
