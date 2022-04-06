import requests
from bs4 import BeautifulSoup
from readabilipy import simple_tree_from_html_string

def scrap(url: str):
    # Get and interprete html code.
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    # For-loop to extract the name of the news source, variable source_name contains string with name
    elements_in_url = url.split('.')
    for i in range(len(elements_in_url)):
        if elements_in_url[i] == "/":
            elements_in_url[i] = elements_in_url[i].replace("/", "")
        if elements_in_url[i][-1] == "/":
            elements_in_url[i] = elements_in_url[i].replace("/", "")
        if elements_in_url[i] == "com" or elements_in_url[i] == "cn" or elements_in_url[i] == "de": 
            source_name = elements_in_url[i-1]
            break
        

    
    links = []

    # print(soup.prettify())
    # print(simple_tree_from_html_string(r.text).prettify())
    
    for l in soup.find_all('a', href=True):
        links.append(l['href'])
    # print(links)


# scrap('https://www.bhaskar.com/')

scrap('https://finance.sina.com.cn/')
# scrap('https://guangming.com') # This site seems to encode html code in some sort a way
# scrap('https://www.amarujala.com/')