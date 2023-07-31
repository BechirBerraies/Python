from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Car :
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.user_id = data_dict['user_id']
        self.model = data_dict['model']
        self.make = data_dict['make']
        self.year = data_dict['year']
        self.created_at = data_dict['created_at']    
        self.updated_at = data_dict['updated_at']    



    # CREATE USER 

    @classmethod 
    def create (cls,data_dict):
        query= """
        INSERT INTO users (user_id,model,make,year,color) VALUES (%(user_id)s,%(model)s,%(make)s,%(year)s,%(color)s);
        """
        #This query 
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    

    # SELECT ALL USERS 

    @classmethod
    def get_all(cls):
        query ="""
        SELECT * FROM users;
    """
        results = connectToMySQL(DATABASE).query_db(query)
        all_cars= []
        for row in results:
            user= cls(row)
            all_cars.append(user)
        #! all_car ; list of objects ; list of instances of the class User : every instance = car
        return all_cars



    #### SELCET ONE USER AND ALL HIS CARS 

    @classmethod




    # SELECT one By Id 
    @classmethod
    def get_by_id(cls,data_dict):
        query = """
        SELECT * FROM cars WHERE id = %(id)s;
"""
        result = connectToMySQL(DATABASE).query_db(query,data_dict)
        # if id exist => list that contains the data of that user
        #[{'id':1 , 'name': 'Jhon wick', created_at :, 'updated_at':}]
        #••••if id not exist
        # () empty 

        if result:

            return cls(result[0])
        return False
