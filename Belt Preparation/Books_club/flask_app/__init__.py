from flask import Flask



app = Flask(__name__)
app.secret_key = "oskot"
DATABASE = "books_club_db"