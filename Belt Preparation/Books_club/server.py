from flask_app import app
# ! Import ALL CONTROLLERS HERE 🚫⛔

from flask_app.controllers import users
from flask_app.controllers import books



if __name__ == '__main__':
    app.run(debug = True, port=5001)