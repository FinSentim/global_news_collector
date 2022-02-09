import unittest
from datetime import date
from GlobalNewsCollector.China.caixin import caixin

class TestCaixin(unittest.TestCase):

    #   Tests that a specific articles infomration matches acutal readable information from website
    def test_get_article(self):
        ncaixin = caixin()
        url = "https://www.caixin.com/2022-01-28/101836280.html"
        #current_date is today's date in format  'DD-MM-YYYY' as string
        current_date = date.today().strftime("%d-%m-%Y")
        correct = {
            'date_publised': '2022-01-28 21:16:17' ,
            'date_retrieved': current_date,
            'url':'https://www.caixin.com/2022-01-28/101836280.html',
            'author': '作者：牛牧江曲',
            'title': '厦门统计局官网称做好房地产税试点准备工作 文章随后删除',
            'publisher':'Caixin Media',
            'publisher_url': 'https://www.caixin.com',
            'body': '【财新网】1月28日，厦门市统计局在官网发布2021年厦门市房地产开发投资运行分析情况。文中提到，要做好房地产税试点落地厦门的前期准备工作，防止房地产市场出现大的波动。几个小时后，该文章显示已被删除。厦门市统计局在上述文章中称，目前当地房地产市场存在的主要问题和困难是销售市场冷热不均、房企拿地意愿下降、商品房销售面积持续低迷。截至2021年末，厦门全市商品房销售面积连续五个月出现负增长，全年比全省平均低10.2个百分点，增幅位居全省倒数第二位。'
        }
        actual = ncaixin.get_article(url)
        self.assertEqual(correct, actual)

    # Test the "structure" of the body section of an article, will fail if website structure changes and scrap not possible
    # This test is more general, since all articles should have at least 20 words worth of reading. Just change
    # the url to test.
    def test_get_article_body(self):
        c = caixin()
        url = "https://www.caixin.com/2022-02-07/101838615.html"
        body = c.get_article(url)['body']
        self.assertGreater(len(body),20)
        
    
    #   Test that all articles from latest news has been scraped
    def test_get_article_list(self):
        c = caixin()
        url = "https://www.caixin.com/"
        actual_length = len(c.get_articles_list(url))
        self.assertEqual(actual_length,28)

    #   Ensure the get_list_article returns a list of dictionaries
    def test_get_article_list_structure(self):
        c = caixin()
        url = "https://www.caixin.com/"
        actual = c.get_articles_list(url)
        for elem in actual:
            self.assertTrue(isinstance(elem, dict))

if __name__ == '__main__':
    unittest.main()


