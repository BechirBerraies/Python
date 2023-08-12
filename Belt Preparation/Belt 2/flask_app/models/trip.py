from flask_app import DATABASE
from flask_app.configs.mysqlconnection import MySQLConnection
from flask import flash


class Trip:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.user_id= data_dict['user_id']
        self.destination = data_dict['destination']
        self.start_date = data_dict['start_date']
        self.end_date = data_dict['end_date']
        self.plan= data_dict['plan']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.poster = ""

    @classmethod 
    def create(cls , data_dict):
        query = """
            INSERT INTO trips (user_id,destination,start_date,end_date,plan) VALUES (%(user_id)s,%(destination)s,%(start_date)s,%(end_date)s,%(plan)s);
            """
        return MySQLConnection(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def get_all(cls,data_dict):
        query="""
        SELECT * FROM trips WHERE user_id = %(id)s;
""" 
        result = MySQLConnection(DATABASE).query_db(query,data_dict)
        all_trips = []
        for row in result:
            trip = cls(row)
            all_trips.append(trip)
        return all_trips
    
    @classmethod
    def get_by_id(cls, data_dict):
        query ="""
        SELECT * FROM trips
        JOIN users 
        ON trips.user_id =users.id
        WHERE trips.id = %(id)s; 
        """
        result = MySQLConnection(DATABASE).query_db(query, data_dict)
        trip = cls(result[0])
        trip.poster = f"{result[0]['first_name']}"
        return trip
    
    @classmethod
    def delete_trip(cls,data_dict):
        query = """
        DELETE FROM trips WHERE id = %(id)s;
"""
        result = MySQLConnection(DATABASE).query_db(query, data_dict)
        return result
    
    @classmethod
    def edit_trip(cls,data_dict):
        query ="""
        UPDATE trips SET destination=%(destination)s , start_date=%(start_date)s, end_date=%(end_date)s , plan=%(plan)s WHERE id =%(id)s;
        """
        result = MySQLConnection(DATABASE).query_db(query, data_dict)
        return result

    @staticmethod
    def validate_trip(data_dict):
        is_valid = True
        if len(data_dict['destination'])< 2:
            flash("A Trip must Consist of at least 3 characters","destination")
            is_valid = False
        if len(data_dict['start_date']) < 1 :
            flash("Insert a start date","start_date")
            is_valid = False
        if len(data_dict['end_date']) <1 :
            flash("Insert an end date .....","end_date")
            is_valid = False
        if len(data_dict['plan']) < 5 :
            flash("A plan must be provided ","plan")
            is_valid = False
        return is_valid