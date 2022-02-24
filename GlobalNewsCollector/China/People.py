import os
import sys
# sys.path.insert(1, os.path.join(sys.path[0], '..'))
# import BaseCollector
from GlobalNewsCollector import BaseCollector
import requests
from bs4 import BeautifulSoup
#from datetime import date
from datetime import datetime

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
        time_consuming_pages = ["society","hb","he","bj","sd","xz","ah","hi"]
        articleInfo = {}
        sort_webpage = url.strip().replace("http://","").split(".")[0]
        
        # To skip long request calls to url, set this variable to True
        skip_time_consuming_articles = True

        if (skip_time_consuming_articles):
            if (sort_webpage in time_consuming_pages):
                return articleInfo
            else:
                r = requests.get(url)
        else:
            r = requests.get(url)

        # Some types of articles have different structures
        if (sort_webpage == "health"):
            soup = BeautifulSoup(r.content, 'html5lib').find('div', attrs={'class': 'articleCont'})
            articleInfo = get_health_article(soup, articleInfo, url)
        elif (sort_webpage == "cpc"):
            soup = BeautifulSoup(r.content, 'html5lib').find('div', attrs={'class': 'p2j_con03 clearfix g-w1200'})
            articleInfo = get_cpc_article(soup, articleInfo, url)
        else:
            soup = BeautifulSoup(r.content, 'html5lib').find('div', attrs={'class': 'layout rm_txt cf'})
            articleInfo = get_basic_article(soup, articleInfo, url)

        # Add shared information thats independent from HTML code
        articleInfo['publisher'] = "Central Committee of the Chinese Communist Party"
        articleInfo['publisher_url'] = "http://www.people.com.cn"
        articleInfo['date_retrieved'] = datetime.utcnow().strftime("%d-%m-%Y %H:%M")
        articleInfo['url'] = url
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
        listOFArticles = soup.find('ul', attrs={'class':'cf blist1'})
        for article in listOFArticles.find_all('li'):
            par = article.find('a', href=True)['href']
            if ("http" in par):
                print(par)
                article = self.get_article(par)
                if (article != {}):
                    articleList.append(article)
            else:
                continue
            #time.sleep(5)
        index = 0
        # for ds in articleList:
        #     if ds=={}:
        #         # print(ds)
        #         # print("index = "+str(index))
        #         articleList.remove(ds)
        #     index = index + 1
        # for index in range(articleList):
        #     if articleList[index]=={}:
        #         # print(ds)
        #         # print("index = "+str(index))
        #         del articleList[index]
        #         # articleList.remove(index)
        #     index = index + 1
        # print(articleList)
        # return articleList.pop()
        
        return articleList


def get_basic_article(soup, articleInfo, url) -> list:
    
    # Retrive information under title and extract date published
    try:
        date_source_info = soup.find('div', attrs={'class': 'col-1-1 fl'}).text.strip().split("|")
    except AttributeError:
        date_source_info = soup.find('div', attrs={'class': 'col-1-1'}).text.strip().split("|")
    articleInfo['date_published'] = format_time(date_source_info[0])
    articleInfo['author'] = extract_author(soup)
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
    
    return articleInfo

def get_health_article(soup, articleInfo, url) -> list:
   
    # Retrive information under title and extract date published
    date_and_source = soup.find('div', attrs={'class': 'artOri'})
    date_and_source.find('a').decompose()
    articleInfo['date_published'] = format_time(date_and_source.text)
    articleInfo['author'] = extract_author(soup)
    articleInfo['title'] = soup.find('div', attrs={'class':'title'}).find('h2').text

    # Extract article info:
    paragraph_table = soup.find('div', attrs={'class':'artDet'})
    body = ""
    # Paragraphs should not have classes
    for paragraph in paragraph_table.find_all('p'):
        # if paragraph['style'] == "text-indent: 2em;":
        body = body + paragraph.text.strip() 
    articleInfo['body'] = body
    return articleInfo

def get_cpc_article(soup, articleInfo, url) -> list:
   
    # Retrive information under title and extract date published
    date_and_source = soup.find('p', attrs={'class': 'sou'})
    date_and_source.find('a').decompose().text
    articleInfo['date_published'] = format_time(date_and_source)
    # Handle missing author articles
    articleInfo['author'] = extract_author(soup)
    articleInfo['title'] = soup.find('div', attrs={'class':'text_c'}).find('h1').text
    # Extract article info:
    paragraph_table = soup.find('div', attrs={'class':'show_text'})
    body = ""
    # Paragraphs should not have classes
    for paragraph in paragraph_table.find_all('p'):
        body = body + paragraph.text.strip() 
    articleInfo['body'] = body
    return articleInfo

def format_time(chinease_time):
    
    chinease_time = chinease_time.strip().replace("来源：", "").replace("年","-").replace("月", "-").replace("日"," ")
    time_element = chinease_time.split(" ")
    hour_min_element = time_element[1].split(":")
    uct_hour = str((int(hour_min_element[0]) - 8 )% 24)
    return time_element[0]+" "+uct_hour+":"+hour_min_element[1]

# Function returns the names inside the "responsible editors"-box. This box seem to always contain the right author and corresponding editor
def extract_author(div):
    try:
        return div.find('div', attrs={'class':'edit cf'}).text.replace("(责编：", "").replace(")","")
    except AttributeError:
        return div.find('div', attrs={'class':'editor'}).text.replace("(责编：", "").replace(")","")


p = People()
oscar=p.get_articles_list("http://www.people.com.cn/")
print(oscar)
# p.get_article("http://cpc.people.com.cn/n1/2022/0216/c164113-32353542.html")