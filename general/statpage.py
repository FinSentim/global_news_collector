

import requests
from bs4 import BeautifulSoup
from readabilipy import simple_json_from_html_string ## requires nodejs version > 10
from readabilipy import simple_tree_from_html_string

# Langue detection libs
from lingua import Language, LanguageDetectorBuilder




def get_article_bytree(url: str):
    # make http request
    r = requests.get(url)

    # fix encoding to handle different langauages
    # r.raise_for_status()
    r.encoding = r.apparent_encoding
    # r.encoding = r.apparent_encoding


    # Send response thruog readabilipy
    tree = simple_tree_from_html_string(r.text)
    # print(tree.prettify())
    title = ""
    article = ""

    # Try to fetch the title
    for h1 in tree.find_all('h1'):
        title = h1
        # print(h1.text)

    if title == "":
        for h2 in tree.find_all('h2'):
            title = h2
            # print(h2.text)
    
    for row in tree.findAll('p'):
        article = article + row.text

    languages = [Language.ENGLISH, Language.HINDI, Language.FRENCH, Language.GERMAN, Language.SPANISH, Language.CHINESE]
    detector = LanguageDetectorBuilder.from_languages(*languages).build()
    print(detector.detect_language_of(article))
    

    print(article)
    


# get_article_bytree('http://world.people.com.cn/n1/2022/0404/c1002-32391390.html')
# get_article_bytree('https://www.aftonbladet.se/nyheter/a/ALV5Pn/ryska-elever-anger-larare-som-kallar-kriget-for-krig')
# print(" ")
# get_article_bytree('https://www.theguardian.com/world/2022/apr/07/turkish-court-sends-case-of-26-accused-over-khashoggi-killing-to-saudi-arabia')
# print(" ")
# get_article_bytree('https://www.manager-magazin.de/finanzen/bundesbank-praesident-joachim-nagel-glaubt-an-baldigen-zinsanstieg-a-58d5345b-db65-4262-ad46-4e447eb955a2')
get_article_bytree('https://hindi.business-standard.com/storypage.php?autono=186301')

















































# req = requests.get('http://world.people.com.cn/n1/2022/0404/c1002-32391390.html')
# req = requests.get('https://www.bhaskar.com/')
req = requests.get('https://www.bhaskar.com/local/uttar-pradesh/agra/news/golden-opportunity-to-make-career-in-hospitality-sector-apply-for-admission-in-heritage-institute-of-hotel-and-tourism-agra-129614083.html')
# req = requests.get('https://www.svd.se/naringsliv/motor')
# req = requests.get('https://www.aftonbladet.se/nyheter/a/ALV5Pn/ryska-elever-anger-larare-som-kallar-kriget-for-krig')
# Fix encoding for non-latin characters
# Changes the encoding for the webpage from utf-8 to GBK
req.raise_for_status()
req.encoding = req.apparent_encoding
# req.encoding = "GBK"

# soup = BeautifulSoup(req.content, 'html5lib')



# article = simple_json_from_html_string(req.text, use_readability=True)

# # s = article['title']
# # p = article['plain_content']
# t = article['plain_text']
# print(t)

# tree = simple_tree_from_html_string(req.text)

# print(tree.prettify())
# print(BeautifulSoup(req.content, 'html5lib'))
# print(BeautifulSoup(req.content, 'html5lib').prettify())
# print(s.decode(encoding='UTF-8'))