from flask_app import DATABASE
from flask_app.configs.mysqlconnection import MySQLConnection
from flask import flash




import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASSWORD_REGEX = re.compile('\d.*[A-Z]|[A-Z].*\d')



class User:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.email = data_dict['email']
        self.password = data_dict['password']
        self.created_at= data_dict['created_at']
        self.updated_at = data_dict['updated_at']


    @classmethod 
    def create(cls , data_dict):
        query = """
            INSERT INTO users (name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
            """
        # print (MySQLConnection(DATABASE).query_db(query,data_dict))
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
    
    @staticmethod
    def validate_register(data_dict):
        is_valid = True
        if len(data_dict['name'])< 2:
            print(" Name too short .....")
            flash(" Name too short .....", "register")
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