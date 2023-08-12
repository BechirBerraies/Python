
from flask_app import DATABASE
from flask_app.configs.mysqlconnection import MySQLConnection
from flask import flash






class Book:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.title = data_dict['title']
        self.num_of_pages = data_dict['num_of_pages']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.author_who_favorited = []
        self.poster = ""

    @classmethod 
    def create(cls , data_dict):
        query = """
            INSERT INTO books (title,num_of_pages) VALUES (%(title)s,%(num_of_pages)s);
            """
        return MySQLConnection(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def get_all(cls):
        query="""
        SELECT * FROM books;
    """ 
        result = MySQLConnection(DATABASE).query_db(query)
        all_books = []
        for row in result:
            book = cls(row)
            book.poster = row['title']
            all_books.append(book)
        return all_books