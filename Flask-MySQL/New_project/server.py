from flask_app import app
from flask_app.controllers import authors , book


# import all controllers here 

if __name__ == '__main__':
    app.run(debug = True, port =5001)