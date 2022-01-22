from abc import ABC, abstractmethod

class BaseCollector(object):
    """
    Base abstract class for all the collectors.
    """

    @abstractmethod
    def get_articles_list(self, url: str) -> list:
        """
        Get the list of articles from the given url.
        ---
        Args:
            url: The url to get the articles list from.
        Returns:
            A list containing the articles.
        """
        pass


    @abstractmethod
    def get_article(self, url: str) -> dict:
        """
        Get the article from the given url.
        ---
        Args:
            url: The url to get the article from.
        Returns:
            A dictionary containing the article.
        """
        pass
    