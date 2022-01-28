# import os
# import sys
# sys.path.insert(1, os.path.join(sys.path[0], '../GlobalNewsCollector/China'))
# from abc import ABC, ABCMeta, abstractmethod
# import caixin
import unittest

# from China import caixin
from GlobalNewsCollector import caixin

class TestCaixin(unittest.TestCase):

    def test_get_article(self):
        # Article one
        caixin = caixin()
        url = "https://www.caixin.com/2022-01-28/101836280.html"
        correct = {
            'date_publised': '2022-01-28 21:16:17' ,
            'date_retrieved': '28-01-2022',
            'url':'https://www.caixin.com/2022-01-28/101836280.html',
            'author': '文｜财新 牛牧江曲',
            'title': '厦门统计局官网称做好房地产税试点准备工作 文章随后删除',
            'publisher':'Caixin Media',
            'publisher_url': 'https://www.caixin.com'
        }
        actual = caixin.get_article(url)
        self.assertEqual(correct, actual)

    def test_get_article_list(self):
        pass
        # url = "https://blog.google/inside-google/googlers/talking-doogler-deserves-round-paws/"
        # blog_body = scrapper.scrap_google_blog(url)
        # self.assertEqual(len(blog_body), 8)
        # for par in blog_body:
        #     self.assertTrue(len(par) > 0)
        #     self.assertIsInstance(par, str)

if __name__ == '__main__':
    unittest.main()
