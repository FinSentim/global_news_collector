import unittest
from GlobalNewsCollector.China.yicai import Yicai
from datetime import datetime

class TestScrapper(unittest.TestCase):

    # Test for get_article
    def test_article(self):
        collector = Yicai()
        url = "https://www.yicai.com/news/101303550.html"
        article = collector.get_article(url)
        self.assertEqual(article['url'], url)
        self.assertEqual(article['date_retrieved'],datetime.today().strftime("%Y-%m-%d"))

    # Test for get_articles_list
    # Note that one could test the amount of articles retrieved only if we change the scrapper to include live articles
    def test_articles_list(self):
        collector = Yicai()
        url = "https://www.yicai.com/"
        list = collector.get_articles_list(url)
        for article in list:
            self.assertTrue(article != None)
            self.assertIsInstance(article, dict)

if __name__ == '__main__':
    unittest.main()