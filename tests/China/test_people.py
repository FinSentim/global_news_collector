import unittest
from datetime import date
from GlobalNewsCollector.China.People import People

# def remove_empty_dicts(dic):
#     for dictionary in dic:
#         if len(dictionary)==0:
#             dic.remove(dictionary)
#     return dic
    

class TestPeople(unittest.TestCase):

     
    c = People()
    
    # Last article empty
    dictionaries = c.get_articles_list("http://www.people.com.cn/")

    # dictionaries = remove_empty_dicts(dictionaries1)
    
    


    # Test the "structure" of the body section of an article, will fail if website structure changes and scrap not possible
    # This test is more general, since all articles should have at least 20 words worth of reading. Just change
    # the url to test.
    def test_get_article_body(self):
        for dictionary in self.dictionaries:
            # if dictionary != {}:
            self.assertGreater(len(dictionary['body']),20)
    
    # Test that author is not an empty string which indicates wrongful extraction from website
    def test_author_structure(self):
        print("HIII:\n")
        # print(self.dictionaries[len(self.dictionaries)-1]
        for dictionary in self.dictionaries:
            if dictionary!={}:
                author = dictionary['author']
                self.assertTrue(author != "")
    
    # Test that title is not an empty string which indicates wrongful extraction from website
    def test_title_structure(self):
        for dictionary in self.dictionaries:
            if dictionary !={}:
                title = dictionary['title']
                self.assertTrue(title != "")
    
    #   Test that atleast a few articles from latest news has been scraped
    # def test_get_article_list(self):
    #     actual_length = len(self.dictionaries)
    #     self.assertGreater(actual_length,5)

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

    def test_date_published_format(self):
        for dictionary in self.dictionaries:
            if dictionary!={}:
                time = dictionary['date_published']
                self.assertRegex(time, "\d+-\d+-\d+ \d+:\d+")
        
   

if __name__ == '__main__':
    unittest.main()


