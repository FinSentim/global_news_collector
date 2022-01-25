from GlobalNewsCollector import BaseCollector

class caixin(BaseCollector):

    # accepts a link to an article and returns a dictionary with the following keys: date_published: date 
    # of publication date_retrieved: date of retrieval url: url of the article title: title of the article 
    # publisher: Company or website that published the article publisher_url: url of the publisher 
    # author: author of the article body: text of the article
    def get_article(self, url: str) -> dict:
        pass
  
    # that accepts a link a page with multiple articles (for example business news page) and returns a 
    # list of dictionaries, where each dictionary is a result of calling get_article(url) on each article 
    # link.
    def get_articles_list(self, url: str) -> list: 
        pass