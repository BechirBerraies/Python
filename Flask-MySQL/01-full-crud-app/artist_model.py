from mysqlconnection import connectToMySQL
    

class Artist : 

    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.nationality = data_dict['nationality']
        self.rate = data_dict['rate']
        self.image = data_dict['image']
        self.is_dead = data_dict['is_dead']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']


    @classmethod
    def get_all(cls):
        query ="SELECT * FROM artists;"
        results = connectToMySQL("artists_schema").query_db(query)
        # print("ballon"*10,results,"ballon"*10)
        all_artists = []
        for row in results:
            artist = cls(row)
            all_artists.append(artist)
        # print(all_artists)
        return all_artists
    
    @classmethod
    def create_artist(cls,data_dict):
        query ="""
        INSERT INTO user(first_name,last_name,nationality,rate ,image,is_dead)
        VALUES (%(first_name)s, %(last_name)s, %(nationality)s, %(rate)s, %(image)s,%(is_dead)s);
        """
        result = connectToMySQL("artists_schema").query_db(query, data_dict)
        # print(result)
        return None
        
    @classmethod 
    def get_one_by_id(cls,data_dict):
        query ="""
            SELECT * FROM artists WHERE id = %(id)s;
"""
        results = connectToMySQL("artists_schema").query_db(query, data_dict)
        artist = cls(results[0])
        print(results, "ballon"*20)

        return artist
    
    @classmethod
    def delete(cls,data_dict):
        query ="""
            DELETE FROM artists WHERE id = %(id)s;
"""
        result = connectToMySQL("artists_schema").query_db(query, data_dict)
        print(result)
        artist = cls(result[0])
        return artist