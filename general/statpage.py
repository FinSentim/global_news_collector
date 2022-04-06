

import requests
from bs4 import BeautifulSoup
from readabilipy import simple_json_from_html_string ## requires nodejs version > 10
from readabilipy import simple_tree_from_html_string
import lxml.html.clean

# req = requests.get('http://world.people.com.cn/n1/2022/0404/c1002-32391390.html')
req = requests.get('https://www.bhaskar.com/')
# Fix encoding for non-latin characters
# Changes the encoding for the webpage from utf-8 to GBK
# req.raise_for_status()
# req.encoding = "GBK"

soup = BeautifulSoup(req.content, 'html5lib')


print()

# test = lxml.html.clean.clean_html('<div><li class="_24e83f49e54ee612"><a href="/db-original/news/mlas-increased-by-900-voters-1000-and-mps-15000-know-how-bjp-reached-here-from-its-first-election-129617639.html"><div class="_02462573" title="BJP का 42 साल का सफर: विधायक 900%, वोटर्स 1000% और सांसद 15000% बढ़े, जानिए अपने पहले चुनाव से BJP यहां तक कैसे पहुंची?"><h3><span style="color: rgb(248, 156, 29);">BJP का 42 साल का सफर:</span> विधायक 900%, वोटर्स 1000% और सांसद 15000% बढ़े, जानिए अपने पहले चुनाव से BJP यहां तक कैसे पहुंची?</h3><figure><picture class="_88c1764a"><source media="(max-width: 768px)" type="image/webp" srcset="https://images.bhaskarassets.com/webp/thumb/256x0/web2images/521/2022/04/05/bjp-sthapna-diwas-timeline-6th-april-cover-2_1649176639.jpg"><source media="(min-width: 768px)" type="image/webp" srcset="https://images.bhaskarassets.com/webp/thumb/256x0/web2images/521/2022/04/05/bjp-sthapna-diwas-timeline-6th-april-cover-2_1649176639.jpg"><img src="https://images.bhaskarassets.com/web2images/521/2022/04/05/bjp-sthapna-diwas-timeline-6th-april-cover-2_1649176639.jpg" alt="विधायक 900%, वोटर्स 1000% और सांसद 15000% बढ़े, जानिए अपने पहले चुनाव से BJP यहां तक कैसे पहुंची?|DB ओरिजिनल,DB Original - Dainik Bhaskar" loading="lazy" class="e86bf44b " width="360" height="270"></picture><div style="display: inline-block; align-items: center; justify-content: center;" class="_986e40ac"><svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M23.9998 3.99999C12.9998 3.99999 3.99976 13 3.99976 24C3.99976 35 12.9998 44 23.9998 44C34.9998 44 43.9998 35 43.9998 24C43.9998 13 34.9998 3.99999 23.9998 3.99999Z" fill="var(--background-color)" fill-opacity="0.7"></path><path d="M31.4 22.6L20.4 16.2C19.4 15.6 18 16.4 18 17.6V30.2C18 31.4 19.4 32.2 20.4 31.6L31.4 25.2C32.4 24.8 32.4 23.2 31.4 22.6Z" fill="var(--foreground-color)"></path><path d="M4.1001 24.0002C4.1001 13.0563 13.0562 4.10017 24.0001 4.10017C34.944 4.10017 43.9001 13.0563 43.9001 24.0002C43.9001 34.944 34.944 43.9002 24.0001 43.9002C13.0562 43.9002 4.1001 34.944 4.1001 24.0002Z" stroke="var(--foreground-color)"></path></svg></div></figure></div></a><div class="ba7566ea"><div><span class="_860009df"><a href="/db-original/">DB ओरिजिनल</a></span></div><ul class="_044f5b5b b8e0b8e7"><li class="_55209b5f _978d7e9d"><button title="विधायक 900%, वोटर्स 1000% और सांसद 15000% बढ़े, जानिए अपने पहले चुनाव से BJP यहां तक कैसे पहुंची?" aria-label="facebook" class="react-share__ShareButton" style="background-color: transparent; border: medium none; padding: 0px; font: inherit; color: inherit; cursor: pointer;"><strong></strong></button></li><li class="_55209b5f fd7bcd8c"><button aria-label="twitter" class="react-share__ShareButton" style="background-color: transparent; border: medium none; padding: 0px; font: inherit; color: inherit; cursor: pointer;"><strong></strong></button></li><li class="_55209b5f e5660928"><strong></strong><span>कॉपी लिंक</span></li></ul><div class="df5ade13"><button aria-label="whatsapp" class="react-share__ShareButton a02745d6 _5b92cdac" style="background-color: transparent; border: medium none; padding: 0px; font: inherit; color: inherit; cursor: pointer;"><strong></strong></button>शेयर</div></div></li></div>')

# print(test)

# clean = lxml.html.clean.clean_html(req.text)

# print(clean)

# print(req.encoding)


# article = simple_json_from_html_string(req.text, use_readability=False)

# s = article['title']
# p = article['plain_content']
# t = article['plain_text']

tree = simple_tree_from_html_string(req.text)

# print(tree.prettify())
# print(BeautifulSoup(req.content, 'html5lib'))
# print(BeautifulSoup(req.content, 'html5lib').prettify())
# print(s.decode(encoding='UTF-8'))