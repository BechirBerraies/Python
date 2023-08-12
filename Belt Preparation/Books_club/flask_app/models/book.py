

from flask_app import DATABASE
from flask_app.configs.mysqlconnection import MySQLConnection
from flask import flash


class Book:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.user_id= data_dict['user_id']
        self.title = data_dict['title']
        self.author = data_dict['author']
        self.thoughts = data_dict['thoughts']
        self.created_at= data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.poster = ""

    @classmethod 
    def create(cls , data_dict):
        query = """
            INSERT INTO books (user_id,title,author,thoughts) VALUES (%(user_id)s,%(title)s,%(author)s,%(thoughts)s);
            """
        print(query)
        return MySQLConnection(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def get_all(cls):
        query="""
        SELECT * FROM books
        JOIN users on books.user_id = users.id;
""" 
        result = MySQLConnection(DATABASE).query_db(query)
        books = []
        for row in result:
            book = cls(row)
            book.poster = row['name']
            books.append(book)
        return books
    


    @classmethod
    def get_by_id(cls, data_dict):
        query ="""
        SELECT * FROM books
        JOIN users 
        On books.user_id =user.id
        WHERE books.id = %(id)s; 
        """
        result = MySQLConnection(DATABASE).query_db(query, data_dict)
        return cls(result[0])
    
    @classmethod
    def update(cls,data_dict):
        query ="""
        UPDATE books SET title=%(title)s , author=%(author)s, thoughts=%(thoughts)s WHERE id =%(id)s;
        """
        result = MySQLConnection(DATABASE).query_db(query, data_dict)
        return result
    
    @classmethod
    def delete_recipe(cls,data_dict):
        query = """
        DELETE FROM recipes WHERE id = %(id)s;
"""
        result = MySQLConnection(DATABASE).query_db(query, data_dict)
        return result
    
    @staticmethod
    def validate_recipe(data_dict):
        is_valid = True
        if len(data_dict['author'])< 2:
            flash("description too short .....","description")
            is_valid = False
        if len(data_dict['title'])< 2:
            flash("instructions too short .....","Instructions")
        if len(data_dict['thoughts']) < 7 :
            flash("Insert a date ","thoughts")
            is_valid = False


        return is_valid
    