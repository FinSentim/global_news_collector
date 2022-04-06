
# from msvcrt import kbhit
import requests 
import re
from bs4 import BeautifulSoup
from readability import Document

def getlinks(url):
    elements_in_url = url.split('.')
    for i in range(len(elements_in_url)):
        if elements_in_url[i] == "/":
            elements_in_url[i] = elements_in_url[i].replace("/", "")
        if elements_in_url[i][-1] == "/":
            elements_in_url[i] = elements_in_url[i].replace("/", "")
        if elements_in_url[i] == "com" or elements_in_url[i] == "cn" or elements_in_url[i] == "de" or elements_in_url[i] == "se": 
            source_name = elements_in_url[i-1]
            break
    links = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    matchCounter = 0
    failCounter = 0
    for l in soup.find_all('a', href=True):
        print(l['href'])
        match = test(l['href'], source_name)
        if (match):
            print("Match")
            print("\n")
            matchCounter += 1
        else:
            failCounter += 1
    print("\n")
    print("#Matches: " + str(matchCounter))
    print('Fails: ' + str(failCounter))
        

def test(url, source_name) -> bool:
    # url = 'http://www.people.cn'
    # links = soup.find_all('a', href=True)
    # for link in links:
    #     print(link['href'])
    
    pattern = '^(http(s)*://).*('+source_name+').*'
    # print(pattern)
    # links = ["https://marreman.com","https://marre.com","https://man.com","https://","https://youtube.com",url]
    # for link in links:
    m = bool(re.match(pattern,url.strip()))
    # print(url)
    # print("Match: "+str(m))
    # print("\n")
    return m

    # print("Title: " + doc.title())
    # print("Body: " + doc.summary())
    

    # title = soup.find_all('meta', attrs={'property':True})
    # # title = soup.find_all("title" in s for s in soup.strings)
    # for t in title:
    #     # if 'title' in t['property']:
    #     #     print (t)
    #     if 'title' in t['property'].lower():
    #         print (t)
         
  
# target url

urls = ['http://www.people.cn']
for url in urls:  
    getlinks(url)
# using the BeaitifulSoup module
# soup = BeautifulSoup(urlopen(url))
  
# # displaying the title
# print("Title of the website is : ")
# print (soup.title.get_text())