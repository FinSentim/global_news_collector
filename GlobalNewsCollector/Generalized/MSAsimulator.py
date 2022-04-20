import random
import datetime

def simulator(list):
    counter = 0
    analyzed_list = []
    for dict in list:
        analyzed_dict = {'article_id' : random.randint(1,20000),
                'company_id' : random.randint(1,200),
                'date_of_publication' : dict['date_published'],
                'date_retrieved': dict['date_retrieved'],
                'url' : dict['url'],
                'title': dict['title'],
                'sentiment': random.uniform(0,1),
                # 'publisher': dict['publisher'],
                'publisher': "Aftonposten",
                'has_content' : 1,
                'author' : dict['author'],
                'country' : dict['language'],
                'language' : dict['language']}
        analyzed_list.append(analyzed_dict)
        counter = counter + 1
    counter = 0
    return analyzed_list