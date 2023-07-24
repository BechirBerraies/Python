from flask import  render_template,redirect,request
from flask_app.controllers.Users_CR import User
from flask_app import app





@app.route('/')
def dashbord():
    allusers= User.get_all()
    print (allusers)
    return render_template('dashbord.html', users = allusers)

@app.route('/users/new')
def newusers():
    return render_template('newusers.html')

@app.route ('/users/create', methods = ['POST'])
def create_user():
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
    }
    User.createuser(data)
    return redirect('/')

@app.route('/users/view/<int:user_id>')
def readuser(user_id):
    data = {'id':user_id}
    users = User.read_one(data)
    return render_template('one_user.html', users = users)


