import unittest
from GlobalNewsCollector.Generalized.GeneralScraper import GeneralScraper
from GlobalNewsCollector.Generalized.LinkPatternMatch import getlinks
import time
import re

class TestGeneralScraper(unittest.TestCase):
    
    time_start = time.time()
    url = "http://www.people.com.cn/"
    c = GeneralScraper()
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
        time_per_article = self.time_elapsed/len(self.dictionaries)
        self.assertLess(time_per_article,2)

    def test_datetime_format(self):
        expected_publication_date_format = '(\d{4}.\d{2}.\d{2})|(\d{2}.\d{2}.\d{4})'
        expected_retrieved_date_format = '\d{2}(-)\d{2}(-)\d{4}(\s)\d{2}(:)\d{2})'
        for d in self.dictionaries:
            publication_date = d['date_published']
            retrieved_date = d['date_retrieved']
            self.assertTrue(bool(re.match(publication_date, expected_publication_date_format)))
            self.assertTrue(bool(re.match(retrieved_date, expected_retrieved_date_format)))

    def test_getlinks(self):
        print("Run test test_getlinks")
        known_good_url = "http://www.people.com.cn/"
        valid_articles = getlinks(known_good_url)
        self.assertGreater(len(valid_articles),0)


    

if __name__ == '__main__':
    unittest.main()