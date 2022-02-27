import unittest
from GlobalNewsCollector.China.People import People

class TestPeople(unittest.TestCase):

     
    c = People()
    dictionaries = c.get_articles_list("http://www.people.com.cn/")

    # Test the "structure" of the body section of an article, will fail if website structure changes and scrap not possible
    # This test is more general, since all articles should have at least 20 words worth of reading. Just change
    # the url to test.
    def test_get_article_body(self):
        for dictionary in self.dictionaries:
            self.assertGreater(len(dictionary['body']),20)
    
    # Test that author is not an empty string which indicates wrongful extraction from website
    def test_author_structure(self):
        for dictionary in self.dictionaries:
            author = dictionary['author']
            self.assertTrue(author != "")
    
    # Test that title is not an empty string which indicates wrongful extraction from website
    def test_title_structure(self):
        for dictionary in self.dictionaries:
            title = dictionary['title']
            self.assertTrue(title != "")

    #   Ensure the get_list_article returns a list of dictionaries
    def test_get_article_list_structure(self):
        for dictionary in self.dictionaries:
            if dictionary!={}:
                self.assertTrue(isinstance(dictionary, dict))

    #   Ensure that time is formatted correctly
    def test_date_retriveved_format(self):
        for dictionary in self.dictionaries:
            if dictionary!={}:
                time = dictionary['date_retrieved']
                self.assertRegex(time, "\d+-\d+-\d+ \d+:\d+")

    #   Ensure that time is formatted correctly
    def test_date_published_format(self):
        for dictionary in self.dictionaries:
            if dictionary!={}:
                time = dictionary['date_published']
                self.assertRegex(time, "\d+-\d+-\d+ \d+:\d+")
        
   

if __name__ == '__main__':
    unittest.main()


