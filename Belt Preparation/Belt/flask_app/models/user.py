from flask_app import DATABASE
from flask_app.configs.mysqlconnection import MySQLConnection
from flask import flash




import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASSWORD_REGEX = re.compile('\d.*[A-Z]|[A-Z].*\d')

class User :
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.password = data_dict['password']
        self.joined_trips = []
    
    @classmethod 
    def create(cls , data_dict):
        query = """
            INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
            """
        # print (MySQLConnection(DATABASE).query_db(query,data_dict))
        return MySQLConnection(DATABASE).query_db(query,data_dict)

    @classmethod
    def add_joined_trips(cls,data_dict):
        query = "INSERT INTO joined (user_id,trip_id) VALUES (%(user_id)s,%(trip_id)s);"
        return MySQLConnection(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def get_by_email(cls,data_dict):
        query ="""
        SELECT * FROM users WHERE email = %(email)s;
        """
        result = MySQLConnection(DATABASE).query_db(query,data_dict)
        if result:
            return cls(result[0])
        return False
    
    @classmethod
    def get_by_id(cls, data_dict):
        query ="""
        SELECT * FROM users WHERE id = %(id)s; 
        """
        result = MySQLConnection(DATABASE).query_db(query, data_dict)
        return cls(result[0])
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users LEFT JOIN joined ON users.id = joined.user_id LEFT JOIN trips ON trips.id = joined.trip_id WHERE users.id = %(id)s;"
        results = MySQLConnection(DATABASE).query_db(query,data)

        # Creates instance of author object from row one
        author = cls(results[0])
        # append all book objects to the instances favorites list.
        for row in results:
            # if there are no favorites
            if row['trips.id'] == None:
                break
            # common column names come back with specific tables attached
            data = {
                "id": row['books.id'],
                "title": row['title'],
                "num_of_pages": row['num_of_pages'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            author.favorite_books.append(book.Book(data))
        return author

    
    @staticmethod
    def validate_register(data_dict):
        is_valid = True
        if len(data_dict['first_name'])< 2:
            print("First Name too short .....")
            flash("First Name too short .....", "register")
            is_valid = False
        if len(data_dict['last_name'])< 2:
            print("First Name too short .....")
            flash("First Name too short .....", "register")
            is_valid = False
        if not EMAIL_REGEX.match(data_dict['email']): 
            flash("Invalid email address!")
            is_valid = False
        elif User.get_by_email({'email':data_dict['email']}):
            flash("Email Already taken . Hope by you !!!! ", "register")
            is_valid = False
        if len(data_dict['password'])< 7:
            print("Password too short .....")
            flash("Password too short .....", "register")
            is_valid = False
        if not PASSWORD_REGEX.match(data_dict['password']):
            flash ("need one uppercase and one number at least")
            is_valid =False
        elif data_dict['password'] != data_dict['confirm_password']:
            print("Password and Confirm password Don't match !!!!!")
            flash("Password and Confirm password Don't match !!!!!", "register")
            is_valid = False
        return is_valid
    

