from flask_app import DATABASE
from flask_app.configs.mysqlconnection import MySQLConnection

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
    return MySQLConnection(DATABASE).query_db(query,data_dict)


