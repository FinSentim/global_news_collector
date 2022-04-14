from curses.ascii import FF
import requests 
import re
from bs4 import BeautifulSoup
from readability import Document

# Ignore links below
# Chinese:
# https://cn.chinadaily.com.cn/
# https://www.caixin.com/?HOLDZH
# http://www.people.com.cn/
# http://www.xinhuanet.com/
# https://www.yicai.com/

# German:
# https://www.manager-magazin.de/

# Website suggestions

# Chinese:
# https://cn.reuters.com/news/china
# https://guangming.com.my/
# https://cn.wsj.com/
# https://finance.sina.com.cn/
# https://www.chinanews.com.cn/finance/

# Indian:
# https://hindi.business-standard.com/
# https://www.jagran.com/
# https://www.bhaskar.com/
# https://www.livehindustan.com/
# https://www.amarujala.com/
# https://www.financialexpress.com/hindi/

# German:
# https://www.handelsblatt.com/
# https://www.dw.com/de/
# https://www.bild.de/
# https://www.finanzen.net/
# https://www.faz.net/aktuell/
# https://www.wiwo.de/

def getlinks(url):
    """
    Find links from frontpage of website that are likely to be articles.
    ---
    Args:
        url: The url of the article of the frontpage.
    Returns: TBD
    """
    domain_types = ["com", "cn", "de", "net", "uk"] # To be updated
    elements_in_url = url.split('.')
    for i in range(len(elements_in_url)):
        if elements_in_url[i] == "/":
            elements_in_url[i] = elements_in_url[i].replace("/", "")
        if elements_in_url[i][-1] == "/":
            elements_in_url[i] = elements_in_url[i].replace("/", "")
        if elements_in_url[i] in domain_types: 
            source_name = elements_in_url[i-1]
            likely_language = elements_in_url[i]
            break

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    matchCounter = 0
    failCounter = 0
    for l in soup.find_all('a', href=True):
        link = l['href']
        if (bool(re.match('^(/).+',link))): # Some valid links don't include main url
            match = filter(url+link, source_name)
        else:
            match = filter(link, source_name)
        print(link)
        if (match):
            print("Match")
            print("\n")
            matchCounter += 1
        else:
            failCounter += 1
    print("\n")
    print("#Matches: " + str(matchCounter))
    print('Fails: ' + str(failCounter))

def filter(url, source_name) -> bool:
    """
    Filter determining if a link is a likely article 
    ---
    Args:
        url: The url of the article of the frontpage.
        source_name: Primary name of source
    Returns: 
        True if link is valid, False if link fails the filters
    """
    match = True
    patternMatch = '^(http(s)*://).*('+source_name+').*' 

    # Will update patternMatches, code currently only uses patternMatch
    # patternMatches = ['^(http(s)*://).*('+source_name+').*', '.*(news).*']

    patternsIgnoreEn = ['^(http(s)*://www.facebook.com).*','^(http(s)*://(www.)*twitter.com).*', '.*(img).*', '.*(video).*', '.*(blog).*', '.*(copyright).*', '.*(help).*','.*(login).*','.*(signup).*','.*(contact).*','.*(about).*','.*(terms-conditions).*','.*(advertise).*','.*(careers).*']
    patternsIgnoreGe = ['.*(datenschutzerklaerung).*','.*(werbung).*','.*(angebote).*','.*(nutzungsrechte).*']
    candidate = re.match(patternMatch,url.strip())
    if (candidate != None):
        candidate = candidate.group(0)
        for pIgnore in patternsIgnoreEn + patternsIgnoreGe:
            if (bool(re.match(pIgnore, candidate))):
                match = False
                # print(candidate + " failed pattern " + pIgnore + "\n")
    else:
        match = False
    return match
         
  


urls = ['https://www.handelsblatt.com/'] 
for url in urls:  
    getlinks(url)
