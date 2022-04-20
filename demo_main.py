from GlobalNewsCollector.Generalized.GeneralScraper import GeneralScraper
from GlobalNewsCollector.Generalized.rds_wrapper import rds_wrapper
from GlobalNewsCollector.Generalized.MSAsimulator import simulator


def run_demo():
    scraper = GeneralScraper()
    # scraped_articles = scraper.get_articles_list('http://www.people.com.cn/')
    scraped_articles = scraper.get_articles_list('https://www.manager-magazin.de/')
    
    # print(scraped_articles)
    # print(len(scraped_articles))

    analysed_articles = simulator(scraped_articles)
    wrapper = rds_wrapper()
    # print("before loop")
    for article in analysed_articles:
        print(article)
        wrapper.article_insert(article)

    
def clear_db():
    wrapper = rds_wrapper()
    for i in range(1,6):
        wrapper.article_delete(i)
    # wrapper.article_delete(2)
    # wrapper.article_delete(3)
    # print(wrapper.article_read(2))

run_demo()
# clear_db()