import unittest
from GlobalNewsCollector.Generalized.GeneralScraper import GeneralScraper

class TestGeneralScraper(unittest.TestCase):
    url = "http://www.people.com.cn/"
    c = GeneralScraper()
    dictionaries = c.get_articles_list(url)
    illegalCharacters = []

    def test_author(self):
        for d in self.dictionaries:
            self.assertFalse
