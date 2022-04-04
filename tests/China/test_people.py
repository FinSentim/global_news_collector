import unittest
from GlobalNewsCollector.China.People import People

class TestPeople(unittest.TestCase):

     
    c = People()
    dictionaries = c.get_articles_list("http://www.people.com.cn/")

    # Some websites contains only pictures and title, therefor tests that the average length of all articles exceeds 20 characters. 
    def test_get_article_body(self):
        tot_lenght = 0
        for dictionary in self.dictionaries:
            tot_lenght = tot_lenght + len(dictionary['body'])
        avg_length = tot_lenght / len(self.dictionaries)
        self.assertGreater(avg_length,20)
    
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


