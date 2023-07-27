from flask_app import app
from flask import render_template , request , redirect , session 
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/create', methods= ['POST'])
def register():
    if User.validate_register(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print("Password :", request.form['password'])
        print("Hashed password :", pw_hash)
        User.create(request.form)
        data_dict ={
            **request.form,
            'password':pw_hash
        }
        print(request.form, "------------")
        print(data_dict,"************")
        return redirect('/dashbord')
    return redirect('/')

@app.route('/dashbord')
def dashbord():
    return render_template("dashbord.html")

@app.route('/login', methods=['POST'])
def login():
    print(request.form)

    user_from_db = User.get_by_email({'email':request.form['email']})
    if user_from_db:
        if not bcrypt.check_password_hash(user_from_db, request.form['password']):
            print("You d'ont have an account")
        print('You have an account')
        return redirect('/dashboard')
    return redirect('/')

