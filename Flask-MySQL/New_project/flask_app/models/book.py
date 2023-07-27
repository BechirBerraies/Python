from flask_app.config.mysqlconnection import connectToMySQL

class book : 
    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.author_id = data_dict['author_id']
        self.title = data_dict['title']
        self.pages = data_dict['pages']
        self.release_year = data_dict['release_year']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']


    