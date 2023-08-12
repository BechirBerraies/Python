from flask_app import DATABASE
from flask_app.configs.mysqlconnection import MySQLConnection
from flask import flash



class Author:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.name= data_dict['name']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.favourite_book = []
        self.poster = ""


    @classmethod 
    def create(cls , data_dict):
        query = """
            INSERT INTO authors (name) VALUES (%(name)s);
            """
        return MySQLConnection(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def get_all(cls):
        query="""
        SELECT * FROM authors;
    """ 
        result = MySQLConnection(DATABASE).query_db(query)
        all_authors = []
        for row in result:
            author = cls(row)
            all_authors.append(author)
        return all_authors
    
    
    @classmethod
    def get_by_id(cls, data_dict):
        query ="""
         "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id 
        LEFT JOIN books ON books.id = favorites.book_id
        WHERE authors.id = %(id)s;"; 
        """
        result = MySQLConnection(DATABASE).query_db(query, data_dict)
        return cls(result[0])