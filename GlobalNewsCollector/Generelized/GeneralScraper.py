from readabilipy import simple_tree_from_html_string
from lingua import Language, LanguageDetectorBuilder
from datetime import datetime
import requests


import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import BaseCollector

# from GlobalNewsCollector import BaseCollector

# Language detection import


class GeneralScraper(BaseCollector.BaseCollector):

    def __init__(self) -> None:
        super().__init__()
        # instantiate the language detector, and decide on what languages it should be able to detect
        # self.languages = [Language.ENGLISH, Language.HINDI, Language.GERMAN, Language.CHINESE, Language.SWEDISH]

        self.acceptedLanguages = ['HINDI', 'GERMAN', 'CHINESE']
        self.detector = LanguageDetectorBuilder.from_all_languages().build()

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
        # Send response through readabilipy
        tree = simple_tree_from_html_string(r.text)

        articleInfo = {}

        title = ""
        body = ""

        # Try to fetch the title
        for h1 in tree.find_all('h1'):
            title = h1.text

        if title == "":
            for h2 in tree.find_all('h2'):
                title = h2.text

        for row in tree.findAll('p'):
            body = body + row.text

        #   Check if body  
        if self.validateArticle(body) != True:
            return {}

        articleInfo['body'] = body
        articleInfo['title'] = title
        articleInfo['url'] = url
        articleInfo['date_retrieved'] = datetime.utcnow().strftime("%d-%m-%Y %H:%M")

        # Detect language, interperet lang as a string and extract language part
        lang = self.detector.detect_language_of(body)
        articleInfo['Language'] = str(lang).split(".")[1]

        return articleInfo
        

    def validateArticle(self, body: str) -> bool:
        valid = False
        lang = self.detector.detect_language_of(body)
        if (str(lang).split('.')[1] in self.acceptedLanguages):
            valid = True
        return valid

        

    


gs = GeneralScraper()
# a = gs.get_article('https://hindi.business-standard.com/storypage.php?autono=186301')
a = gs.get_article('https://www.manager-magazin.de/finanzen/bundesbank-praesident-joachim-nagel-glaubt-an-baldigen-zinsanstieg-a-58d5345b-db65-4262-ad46-4e447eb955a2')

# for key in a.values():
#     print(key)
#     print(" ")


    
