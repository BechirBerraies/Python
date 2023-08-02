from flask_app import DATABASE
from flask_app.configs.mysqlconnection import MySQLConnection
from flask import flash

class User :
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.password = data_dict['password']
    
    @classmethod 
    def create(cls , data_dict):
        query = """
            INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
            """
        print (MySQLConnection(DATABASE).query_db(query,data_dict))
        return MySQLConnection(DATABASE).query_db(query,data_dict)
    
    @staticmethod
    def validate_register(data_dict):
        is_valid = True
        if len(data_dict['first_name'])< 2:
            print("First Name too short .....")
            flash("First Name too short .....", "register")
            is_valid = False
        if len(data_dict['last_name'])< 2:
            print("Last Name too short .....")
            flash("Last Name too short .....", "register")
            is_valid = False
        if len(data_dict['email'])<2 :
            print("Email is too short ....")
            flash("Email is too short ... ", "register")
        if len(data_dict['password'])< 7:
            print("Password too short .....")
            flash("Password too short .....", "register")
            is_valid = False

        return is_valid