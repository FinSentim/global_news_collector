import requests 
import re
from bs4 import BeautifulSoup


def getlinks(url) -> list:
    """
    Find links from frontpage of website that are likely to be articles.
    ---
    Args:
        url: The url of the article of the frontpage.
    Returns: List of valid articles
    """

    # Add supported domain types
    domain_types = ["com", "cn", "de", "net", "uk"] 

    # Find likely language by identifying domain type, and get source name
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
    printMatches = False
    validLinks = []
    for l in soup.find_all('a', href=True):
        link = l['href']
        if (bool(re.match('^(/).+',link))): # Some valid links don't include main part of url
            link = url+link
            match = filter(link, source_name, likely_language="com")
        else:
            match = filter(link, source_name, likely_language="com")
        if (match):
            validLinks.append(link)
        if (printMatches):
            print(link)
            if (match):
                print("Match")
                print("\n")
                matchCounter += 1
            else:
                failCounter += 1
    if (printMatches):
        print("\n")
        print("#Matches: " + str(matchCounter))
        print('Fails: ' + str(failCounter))
    
    return validLinks


def filter(url, source_name, likely_language) -> bool:
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
    patternsIgnoreGe = ['.*(datenschutzerklaerung).*','.*(werbung).*','.*(angebote).*','.*(nutzungsrechte).*','.*(nutzungshinweise).*','.*(nutzungsbedingungen).*']
    patternsIgnore = []
    
    # Currently only supports german links, as majority links uses english, can be extended for other languages
    if (likely_language == "de"):
        patternsIgnore = patternsIgnoreGe
    
    
    candidate = re.match(patternMatch,url.strip())
    printSuccessfullyFiltered = False
    if (candidate != None):
        candidate = candidate.group(0)
        for pIgnore in patternsIgnoreEn + patternsIgnore:
            if (bool(re.match(pIgnore, candidate))):
                match = False
                if (printSuccessfullyFiltered):
                    print(candidate + " failed pattern " + pIgnore + "\n")
    else:
        match = False
    return match
         
  


# urls = ['http://www.people.com.cn/'] 
# for url in urls:  
#     getlinks(url)
