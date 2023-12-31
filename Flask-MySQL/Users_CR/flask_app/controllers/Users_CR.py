from flask_app.config.mysqlconnection import connectToMySQL

class User : 
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('UserCR_schema').query_db(query)
        alluser = []
        for user in results:
            alluser.append(cls(user))
        return alluser

    @classmethod
    def createuser(cls,data):
        query="""
    INSERT INTO users(first_name,last_name,email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s);
        """
        result = connectToMySQL("UserCR_schema").query_db(query, data)
        return None

    @classmethod
    def read_one(cls,data):
        query = """
        SELECT *  FROM users WHERE id = %(id)s ; 
        """
        
        result = connectToMySQL("UserCR_schema").query_db(query,data)
        return cls(result[0])