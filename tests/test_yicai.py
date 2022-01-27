import unittest
from GlobalNewsCollector import yicai
from datetime import date

class TestScrapper(unittest.TestCase):

    def test_article(self):
        collector = yicai()
        url = "https://www.yicai.com/news/101303550.html"
        article = collector.get_article(url)
        dictionary = {
            'date_published': "2022-01-27 16:54:25",
            'date_retrieved': date.today().strftime("%d %b %Y"),
            'url' : url,
            'title': "就地过年引发年货春运热潮，年前异地“孝心单”猛增",
            'publisher': 'yicai',
            'publisher_url': 'https://www.yicai.com/',
            'author': "陆涵之",
            'body': 
        }
        self.assertEqual(article, dictionary)

    def test_article_list(self):
        collector = yicai()
        url = "https://www.yicai.com/"
        list = collector.get_article_list(url)
        self.assertEqual(len(list), 25)
        for par in list:
            self.assertTrue(len(par) > 0)
            self.assertIsInstance(par, str)

if __name__ == '__main__':
    unittest.main()