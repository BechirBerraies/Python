from flask import Flask, render_template,redirect,request
from Users_CR import user


app = Flask(__name__)
@app.route('/')
def dashbord():
    allusers= user.get_all()
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
    user.createuser(data)
    return redirect('/')





if __name__ == '__main__':
    app.run(debug=True,port=5001)