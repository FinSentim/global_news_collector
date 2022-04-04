

import requests
from bs4 import BeautifulSoup
from readabilipy import simple_json_from_html_string ## requires nodejs version > 10
from readabilipy import simple_tree_from_html_string


# req = requests.get('http://world.people.com.cn/n1/2022/0404/c1002-32391390.html')
req = requests.get('https://www.bhaskar.com/')
# Fix encoding for non-latin characters
# Changes the encoding for the webpage from utf-8 to GBK
# req.raise_for_status()
# req.encoding = "GBK"

print(req.encoding)


# article = simple_json_from_html_string(req.text, use_readability=False)

# s = article['title']
# p = article['plain_content']
# t = article['plain_text']

tree = simple_tree_from_html_string(req.text)

# print(tree.prettify())
# print(BeautifulSoup(req.content, 'html5lib'))
# print(BeautifulSoup(req.content, 'html5lib').prettify())
# print(s.decode(encoding='UTF-8'))