from flask_app import DATABASE
from flask_app.configs.mysqlconnection import MySQLConnection
from flask import flash


class Recipe:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.user_id= data_dict['user_id']
        self.name = data_dict['name']
        self.description = data_dict['description']
        self.Under_30 = data_dict['Under_30']
        self.Instructions= data_dict['Instructions']
        self.Date_made = data_dict['Date_made']
        self.poster = ""

    @classmethod 
    def create(cls , data_dict):
        query = """
            INSERT INTO recipes (user_id,name,description,Under_30,instructions,Date_made) VALUES (%(user_id)s,%(name)s,%(description)s,%(Under_30)s,%(Instructions)s,%(Date_made)s);
            """
        return MySQLConnection(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def get_all(cls):
        query="""
        SELECT * FROM recipes
        JOIN users on recipes.user_id = users.id;
""" 
        result = MySQLConnection(DATABASE).query_db(query)
        all_recipes = []
        for row in result:
            recipe = cls(row)
            recipe.poster = f"{row['first_name']} {row['last_name']}"
            all_recipes.append(recipe)
        return all_recipes
    


    @classmethod
    def get_by_id(cls, data_dict):
        query ="""
        SELECT * FROM recipes
        JOIN users 
        ON recipes.user_id =users.id
        WHERE recipes.id = %(id)s; 
        """
        result = MySQLConnection(DATABASE).query_db(query, data_dict)
        recipe = cls(result[0])
        recipe.poster = f"{result[0]['first_name']}"
        return recipe
    
    @classmethod
    def edit_recipe(cls,data_dict):
        query ="""
        UPDATE recipes SET name=%(name)s , description=%(description)s, Under_30=%(Under_30)s , Instructions=%(Instructions)s,Date_made=%(Date_made)s  WHERE id =%(id)s;
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
        if len(data_dict['name'])< 2:
            flash(" Name too short .....","name")
            is_valid = False
        if len(data_dict['description'])< 2:
            flash("description too short .....","description")
            is_valid = False
        if len(data_dict['Instructions'])< 2:
            flash("instructions too short .....","Instructions")
            is_valid =False
        if len(data_dict['Date_made']) < 1 :
            flash("Insert a date ","Date_made")
            is_valid = False


        return is_valid
    