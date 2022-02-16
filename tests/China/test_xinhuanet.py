import unittest
from GlobalNewsCollector.China.Xinhuanet import Xinhuanet
from datetime import date

class Test_XinhuanetScrapper(unittest.TestCase):

    def test_get_articles_list(self):
        url = "http://www.xinhuanet.com/"
        list = Xinhuanet.get_articles_list(Xinhuanet,url)
        self.assertFalse(list == None)
        for article in list:
            self.assertTrue("http://www.news.cn" in article["url"])
            self.assertTrue(len(article) > 0)
            self.assertIsInstance(article, dict)

        

    def test_get_article(self):
        
        urlList = Xinhuanet.get_articles_list(Xinhuanet,"http://www.xinhuanet.com/")
        url = urlList[0]["url"]
        article = Xinhuanet.get_article(Xinhuanet,url)
        
        self.assertTrue(len(article) == 8) #Checking that dictionary article contains 8 components. 
        self.assertIsInstance(article, dict)

        for item in article: 
            self.assertFalse(item == None)
            self.assertFalse(item == "") 

        self.assertTrue(len(article["body"]) > 10)
        
       

if __name__ == '__main__':
    unittest.main()