from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE




class Dojo : 
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']



    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM dojos;
"""
        result = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for row in result :
            dojos = cls(row)
            all_dojos.append(dojos)
        return all_dojos
    
    @classmethod 
    def create(cls,data_dict):
        query = """
        INSERT INTO dojos (name) VALUES (%(name)s);
"""
        result = connectToMySQL(DATABASE).query_db(query,data_dict  )
        return result