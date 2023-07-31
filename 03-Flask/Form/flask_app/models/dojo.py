from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash



class Dojo:
    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.location = data_dict['location']
        self.language = data_dict['language']
        self.comment = data_dict['comment']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']


    @classmethod
    def create(cls,data_dict):
        query = """
        INSERT INTO dojos (name,location,language,comment) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s)
        """
        result = connectToMySQL(DATABASE).query_db(query,data_dict)
        print(result, "++++"*20)
        return result

    @classmethod
    def show_by_id(cls, data_dict):
        query = """
                SELECT * FROM dojos WHERE id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query,data_dict)
        print("##########@"*20,result)
        return cls(result[0])


    
    @staticmethod
    def validate_Dojo(data_dict):
        is_valid = True 
        if len(data_dict['name'])<2:
            print("First Name too short .....")
            flash("First Name too short .....", "register")
        is_valid = False
        if data_dict['location'] == "Default Select" :
            print("Location required")
            flash("Location Required", "register")
        is_valid =False 

        return is_valid
