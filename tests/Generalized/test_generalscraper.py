import unittest
from GlobalNewsCollector.Generalized.GeneralScraper import GeneralScraper
from GlobalNewsCollector.Generalized.LinkPatternMatch import getlinks
import time
import re
import random

class TestGeneralScraper(unittest.TestCase):
    urls = {"CHINESE":["http://www.people.com.cn/", "https://www.yicai.com/", "http://www.xinhuanet.com/", "https://www.caixin.com/", "https://cn.chinadaily.com.cn/", ],"GERMAN":["https://www.manager-magazin.de/", "https://www.handelsblatt.com/", "https://www.finanzen.net/", "https://www.bild.de/", "https://www.wiwo.de/"],"HINDI":["https://hindi.business-standard.com/", "https://www.jagran.com/", "https://www.bhaskar.com/", "https://www.livehindustan.com/", "https://www.amarujala.com/"]}
    keysIndex = list(urls)
    languageIndex = random.randint(0,2)
    language = keysIndex[languageIndex]
    website = random.randint(0,4)
    url = urls[language][website]
    c = GeneralScraper()
    amount_of_articles = len(getlinks(url))
    time_start = time.time()
    dictionaries = c.get_articles_list(url)
    time_end = time.time()
    time_elapsed = time_end - time_start
    non_alphabetical = ['_','0','1','2','3','4','5','6','7','8','9']

    def test_get_article_author(self):
        print("Run test test_get_article_author")
        for d in self.dictionaries:
            author = d['author']
            for n_a in self.non_alphabetical:
                self.assertFalse(n_a in author)
            
    def test_get_article_body(self):
        print("Run test test_get_article_body")
        body_length = 0
        for dictionary in self.dictionaries:
            body_length = len(dictionary['body'])
            self.assertGreaterEqual(body_length,100)   
    
    def test_get_article_title(self):
        print("Run test test_get_article_title")
        title_length = 0
        for dictionary in self.dictionaries:
            title_length = len(dictionary['title'])
            self.assertGreater(title_length,0)

    def test_scraper_performance(self):
        print("Run test test_scraper_performance")
        time_per_article = self.time_elapsed/self.amount_of_articles
        print(time_per_article)
        self.assertLess(time_per_article,2)

    def test_datetime_format(self):
        expected_publication_date_format = '(\d{4}.\d{2}.\d{2})|(\d{2}.\d{2}.\d{4})'
        expected_retrieved_date_format = '\d{2}(-)\d{2}(-)\d{4}(\s)\d{2}(:)\d{2}'
        for d in self.dictionaries:
            publication_date = d['date_published']
            if (publication_date != ""):
                self.assertTrue(bool(re.match(expected_publication_date_format, publication_date)))
            retrieved_date = str(d['date_retrieved'])
            self.assertTrue(bool(re.match(expected_retrieved_date_format, retrieved_date)))


    def test_get_language(self):
        for d in self.dictionaries:
            language = d['language']
            self.assertEqual(language,self.language)

    def test_getlinks(self):
        print("Run test test_getlinks")
        known_good_url = "http://www.people.com.cn/"
        valid_articles = getlinks(known_good_url)
        self.assertGreater(len(valid_articles),0)


    

if __name__ == '__main__':
    unittest.main()