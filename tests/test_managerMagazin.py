import unittest
from GlobalNewsCollector.Germany.managerMagazin import managerMagazin
from datetime import date

class TestScrapper(unittest.TestCase):

    def test_get_articles_list(self):
        pass

    def test_get_article(self):
        url = "https://www.manager-magazin.de/harvard/selbstmanagement/selbstmanagement-wie-man-sich-dazu-bringt-schwierige-dinge-anzugehen-a-115ecb8c-9380-45d3-9ed6-9a00897259f2"
        dict = managerMagazin.get_article(url)
        correct_dict = {"date_published" = []}
        pass
       

if __name__ == '__main__':
    unittest.main()