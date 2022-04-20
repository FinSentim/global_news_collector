import requests 
import re
from bs4 import BeautifulSoup


def getlinks(url: str) -> list:
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
    match_counter = 0
    fail_counter = 0
    print_matches = False
    valid_links = []
    for l in soup.find_all('a', href=True):
        link = l['href']
        if (bool(re.match('^(/).+',link))): # Some valid links don't include main part of url
            link = url+link
            match = filter(link, source_name, likely_language="com")
        else:
            match = filter(link, source_name, likely_language="com")
        if (match):
            valid_links.append(link)
        if (print_matches):
            print(link)
            if (match):
                print("Match")
                print("\n")
                match_counter += 1
            else:
                fail_counter += 1
    if (print_matches):
        print("\n")
        print("#Matches: " + str(match_counter))
        print('Fails: ' + str(fail_counter))
    
    return valid_links


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
    pattern_match = '^(http(s)*://).*('+source_name+').*' 

    # Will update pattern_matches, code currently only uses pattern_match
    # pattern_matches = ['^(http(s)*://).*('+source_name+').*', '.*(news).*']
    patterns_ignore_en = ['^(http(s)*://www.facebook.com).*','^(http(s)*://(www.)*twitter.com).*', '.*(img).*', '.*(video).*', '.*(blog).*', '.*(copyright).*', '.*(help).*','.*(login).*','.*(signup).*','.*(contact).*','.*(about).*','.*(terms-conditions).*','.*(advertise).*','.*(careers).*']
    patterns_ignore_ge = ['.*(datenschutzerklaerung).*','.*(werbung).*','.*(angebote).*','.*(nutzungsrechte).*','.*(nutzungshinweise).*','.*(nutzungsbedingungen).*']
    patterns_ignore = []
    
    # Currently only supports german links, as majority links uses english, can be extended for other languages
    if (likely_language == "de"):
        patterns_ignore = patterns_ignore_ge
    
    
    candidate = re.match(pattern_match,url.strip())
    print_successfully_filtered = False
    if (candidate != None and candidate.group(0).count('/') > 3):
        candidate = candidate.group(0)
        for p_ignore in patterns_ignore_en + patterns_ignore:
            if (bool(re.match(p_ignore, candidate))):
                match = False
                if (print_successfully_filtered):
                    print(candidate + " failed pattern " + p_ignore + "\n")
    else:
        match = False
    return match
         
  


# urls = ['http://www.people.com.cn/'] 
# for url in urls:  
#     getlinks(url)
