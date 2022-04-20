#username: admin
#pass: RLnSEs2EPwFzibi
#address: database-2-instance-1.cwar6wtzs7mw.eu-north-1.rds.amazonaws.com
#coding: utf-8
from sqlalchemy import create_engine, table, insert, update, select, MetaData, delete

class rds_wrapper:

    def __init__(self) -> None:
        engine = create_engine('mysql+pymysql://admin:RLnSEs2EPwFzibi@database-2-instance-1.cwar6wtzs7mw.eu-north-1.rds.amazonaws.com:3306/db_news', echo = True)
        # global conn 
        self.conn = engine.connect()

        metadata = MetaData(engine)
        metadata.reflect()
        self.table = metadata.tables['tblNewsArticlesGlobal']

    def article_insert(self, dict):
        print("inside insert")
        stmt = (
            insert(self.table)
            .values(    
                        article_id = dict.get("article_id"),
                        company_id = dict.get("company_id"),
                        date_published = dict.get("date_of_publication"),
                        date_retrieved = dict.get("date_retrieved"),
                        source_url = dict.get("url"),
                        title = dict.get("title"), 
                        sentiment = dict.get("sentiment"),
                        publisher = dict.get("publisher"),
                        has_content = 1,
                        author = dict.get("author"),
                        country = dict.get("country"),
                        language = dict.get("language"),
                    )
        )
        result = self.conn.execute(stmt)

    def article_update(self, dict):
        stmt = (
            update(self.table)
            .values(
                        article_id = dict.get("article_id"),
                        company_id = dict.get("company_id"),
                        date_published = dict.get("date_of_publication"),
                        date_retrieved = dict.get("date_retrieved"),
                        source_url = dict.get("url"),
                        title = dict.get("title"), 
                        sentiment = dict.get("sentiment"),
                        publisher = dict.get("publisher"),
                        has_content = 1,
                        author = dict.get("author"),
                        country = dict.get("country"),
                        language = dict.get("language"),
                    )
            .where(self.table.c.article_id == dict.get("article_id"))
        )
        result = self.conn.execute(stmt)

    def article_read(self, article_id):
        stmt = (
            select([self.table])
            .where(self.table.c.article_id == article_id)
        )
        result = self.conn.execute(stmt)
        return result.fetchone()

    def article_delete(self, article_id):
        stmt = (
            delete(self.table)
            .where(self.table.c.article_id == article_id)
        )
        result = self.conn.execute(stmt) 