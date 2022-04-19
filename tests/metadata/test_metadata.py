
   def test_article(self):
        collector = Yicai()
        url = "https://www.yicai.com/news/101303550.html"
        article = collector.get_article(url)
        self.assertEqual(article['url'], url)
        self.assertEqual(article['date_retrieved'],datetime.utcnow().strftime("%Y-%m-%d"))






if __name__ == '__main__':
    unittest.main()