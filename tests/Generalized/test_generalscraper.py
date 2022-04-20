import unittest
from GlobalNewsCollector.Generalized.GeneralScraper import GeneralScraper
from GlobalNewsCollector.Generalized.LinkPatternMatch import getlinks

class TestGeneralScraper(unittest.TestCase):
    url = "http://www.people.com.cn/"
    c = GeneralScraper()
    dictionaries = c.get_articles_list(url)
    non_alphabetical = ['_','0','1','2','3','4','5','6','7','8','9']

    def test_get_article_author(self):
        for d in self.dictionaries:
            author = d['author']
            for n_a in self.non_alphabetical:
                self.assertFalse(n_a in author)
            
    def test_get_article_body(self):
        tot_lenght = 0
        for dictionary in self.dictionaries:
            tot_lenght = tot_lenght + len(dictionary['body'])
        avg_length = tot_lenght / len(self.dictionaries)
        self.assertGreater(avg_length,20)

    def test_getlinks(self):
        known_good_url = "http://www.people.com.cn/"
        valid_articles = getlinks(known_good_url)
        self.assertGreater(len(valid_articles),0)

if __name__ == '__main__':
    unittest.main()