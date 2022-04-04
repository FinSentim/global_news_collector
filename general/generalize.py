

import requests
from bs4 import BeautifulSoup
from readabilipy import simple_json_from_html_string ## requires nodejs version > 10
from readabilipy import simple_tree_from_html_string
# req = requests.get('https://en.wikipedia.org/wiki/Readability')
#req = requests.get('http://world.people.com.cn/n1/2022/0404/c1002-32391390.html')
req = requests.get('https://www.svt.se/nyheter/utrikes/krigsvetaren-om-de-dodade-i-butja-sjalvklart-ar-det-ett-krigsbrott')
#Needed to work with non latin characters
req.raise_for_status()
req.encoding = "GBK"


article = simple_json_from_html_string(req.text, use_readability=True)
tree = simple_tree_from_html_string(req.text)
s = article['title']
p = article['plain_content']
t = article['plain_text']

print(t)
# print(BeautifulSoup(req.content, 'html5lib'))
# print(BeautifulSoup(req.content, 'html5lib').prettify())
# print(s.decode(encoding='UTF-8'))