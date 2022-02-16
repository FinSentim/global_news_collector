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
        sort_webpage = url.replace("http://","").split(".")[0]
        print("sökord i url: " + sort_webpage)
        r = requests.get(url)
        # soup = BeautifulSoup(r.content, 'html5lib').find('div', attrs={'class': 'layout rm_txt cf'})
        articleInfo = {}

        if (sort_webpage == "health"):
            soup = BeautifulSoup(r.content, 'html5lib').find('div', attrs={'class': 'articleCont'})
            articleInfo = get_health_article(soup, articleInfo, url)
            pass
        elif (sort_webpage == "cpc"):
            soup = BeautifulSoup(r.content, 'html5lib').find('div', attrs={'class': 'p2j_con03 clearfix g-w1200'})
            articleInfo = get_cpc_article(soup, articleInfo, url)
        else:
            soup = BeautifulSoup(r.content, 'html5lib').find('div', attrs={'class': 'layout rm_txt cf'})
            print("Now calling get_basic_article")
            articleInfo = get_basic_article(soup, articleInfo, url)

    #     # Retrive information under title and extract date published
    #     try:
    #         date_source_info = soup.find('div', attrs={'class': 'col-1-1 fl'}).text.strip().split("|")
    #     except AttributeError:
    #         date_source_info = soup.find('div', attrs={'class': 'col-1-1'}).text.strip().split("|")
    #     articleInfo['date_published'] = date_source_info[0]
    #     articleInfo['date_retrieved'] = date.today().strftime("%d-%m-%Y")
    #     articleInfo['url'] = url

    #     # Handle missing author articles
    #     try:
    #         articleInfo['author'] = soup.find('div', attrs={'class':'author cf'}).text 
    #     except AttributeError:
    #         articleInfo['author'] = 'N/A'    
    #     try:
    #         articleInfo['title'] = soup.find('div', attrs={'class':'col col-1 fl'}).find('h1').text
    #     except AttributeError:
    #         articleInfo['title'] = soup.find('div', attrs={'class':'col col-1'}).find('h1').text

    #     articleInfo['publisher'] = "Central Committee of the Chinese Communist Party"
    #     articleInfo['publisher_url'] = "http://www.people.com.cn" 

    #     # Extract article info:
    #     paragraph_table = soup.find('div', attrs={'class':'rm_txt_con cf'})
    #     body = ""
    #     # Paragraphs should not have classes
    #     for paragraph in paragraph_table.find_all('p'):
    #         try:
    #             ignore = paragraph['class']
    #         except KeyError:
    #             body = body + paragraph.text.strip()
        
    #     articleInfo['body'] = body
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

        # Start extraxting articles from "hotspot" - section
        listOFArticles = soup.find('div', attrs={'class':'list2 cf'})
        for article in listOFArticles.find_all('li'):
            par = article.find('a', href=True)['href']
            print(par)
            articleList.append(self.get_article(par))
            
        print(articleList)
        return articleList


def get_basic_article(soup, articleInfo, url) -> list:
    # print("Inne i get_basic_article")
    # Retrive information under title and extract date published
    try:
        date_source_info = soup.find('div', attrs={'class': 'col-1-1 fl'}).text.strip().split("|")
    except AttributeError:
        date_source_info = soup.find('div', attrs={'class': 'col-1-1'}).text.strip().split("|")
    articleInfo['date_published'] = date_source_info[0]
    articleInfo['date_retrieved'] = date.today().strftime("%d-%m-%Y")
    articleInfo['url'] = url

    # Handle missing author articles
    try:
        articleInfo['author'] = soup.find('div', attrs={'class':'author cf'}).text 
    except AttributeError:
        articleInfo['author'] = 'N/A'    
    try:
        articleInfo['title'] = soup.find('div', attrs={'class':'col col-1 fl'}).find('h1').text
    except AttributeError:
        articleInfo['title'] = soup.find('div', attrs={'class':'col col-1'}).find('h1').text

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
    # print(articleInfo)
    return articleInfo

def get_health_article(soup, articleInfo, url) -> list:
   
    # Retrive information under title and extract date published
    date_and_source = soup.find('div', attrs={'class': 'artOri'})
    date_and_source.find('a').decompose()
    date_and_time = date_and_source.text.strip().replace("来源：", "GMT+8").replace("年","-").replace("月", "-").replace("日","")
    articleInfo['date_published'] = date_and_time
    articleInfo['date_retrieved'] = date.today().strftime("%d-%m-%Y")   
    articleInfo['url'] = url

    # Handle missing author articles
    try:
        articleInfo['author'] = soup.find('div', attrs={'class':'author cf'}).text 
    except AttributeError:
        articleInfo['author'] = 'N/A'    
    try:
        articleInfo['title'] = soup.find('div', attrs={'class':'title'}).find('h2').text
    except AttributeError:
        articleInfo['title'] = soup.find('div', attrs={'class':'col col-1'}).find('h1').text

    articleInfo['publisher'] = "Central Committee of the Chinese Communist Party"
    articleInfo['publisher_url'] = "http://www.people.com.cn" 

    # Extract article info:
    paragraph_table = soup.find('div', attrs={'class':'artDet'})
    body = ""
    # Paragraphs should not have classes
    for paragraph in paragraph_table.find_all('p'):
        if paragraph['style'] == "text-indent: 2em;":
            body = body + paragraph.text.strip() 
        else: 
            pass
    
    articleInfo['body'] = body
    # print(articleInfo)
    return articleInfo

def get_cpc_article(soup, articleInfo, url) -> list:
   
    # Retrive information under title and extract date published
    date_and_source = soup.find('p', attrs={'class': 'sou'})
    date_and_source.find('a').decompose()
    date_and_time = date_and_source.text.strip().replace("来源：", "GMT+8").replace("年","-").replace("月", "-").replace("日","").replace("\xa0\xa0\xa0\xa0"," ")
    articleInfo['date_published'] = date_and_time
    articleInfo['date_retrieved'] = date.today().strftime("%d-%m-%Y")   
    articleInfo['url'] = url

    # Handle missing author articles
    try:
        articleInfo['author'] = soup.find('div', attrs={'class':'author cf'}).text 
    except AttributeError:
        articleInfo['author'] = 'N/A'    
    try:
        articleInfo['title'] = soup.find('div', attrs={'class':'text_c'}).find('h1').text
    except AttributeError:
        articleInfo['title'] = soup.find('div', attrs={'class':'col col-1'}).find('h1').text

    articleInfo['publisher'] = "Central Committee of the Chinese Communist Party"
    articleInfo['publisher_url'] = "http://www.people.com.cn" 

    # Extract article info:
    paragraph_table = soup.find('div', attrs={'class':'show_text'})
    body = ""
    # Paragraphs should not have classes
    for paragraph in paragraph_table.find_all('p'):
        body = body + paragraph.text.strip() 
        
    
    articleInfo['body'] = body
    # print(articleInfo)
    return articleInfo

p = People()
p.get_articles_list("http://www.people.com.cn/")
# p.get_article("http://cpc.people.com.cn/n1/2022/0216/c164113-32353542.html")