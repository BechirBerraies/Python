from flask_app import app
from flask import render_template , request, redirect,session, flash
from flask_app.models.user import User 
from flask_app.models.book import Book 


from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route('/')
def register():
    return render_template("login.html")


@app.route('/dashbord')
def dashbord():
    if 'user_id' not in session:
        return redirect('/')
    logged_user = User.get_by_id({'id':session['user_id']})
    all_books = Book.get_all()
    return render_template("dashbord.html", logged_user =logged_user, all_books = all_books)



@app.route('/users/create', methods = ['POST'])
def create_user():
    if User.validate_register(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print("PASSWORD : ", pw_hash)
        data_dict = {
            ** request.form,
            'password':pw_hash
        }
        user_id = User.create(data_dict)
        print(request.form)
        session['user_id'] = user_id
        return redirect('/dashbord')
    return redirect('/')

@app.route('/login' , methods =['POST'])
def login():
    user_from_db = User.get_by_email({'email':request.form['email']})
    print(user_from_db) 
    if user_from_db:
        if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
    # if we get False after checking the password
            flash("Wrong Password !!!","login")
            return redirect('/')
        session['user_id'] = user_from_db.id
        return redirect('/dashbord')
    flash("Wrong email !!!!","login")
    return redirect('/')


@app.route('/logout', methods =['POST'])
def logout():
    session.clear()
    return redirect('/')
