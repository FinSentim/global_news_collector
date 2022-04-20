import random
import datetime
counter = 0
def simulator(list):
    for dict in list:
        dict = {'article_id' : counter,
                'company_id' : random.randint(1,200),
                'date_of_publication' : dict['date_published'],
                'date_retrieved': dict['date_retrieved'],
                'url' : dict['url'],
                'title': dict['title'],
                'sentiment': random.uniform(0,1),
                'publisher': dict['publisher'],
                'has_content' : 1,
                'author' : dict['author'],
                'country' : dict['language'],
                'language' : dict['language']}
        counter = counter + 1
    counter = 0
    return list