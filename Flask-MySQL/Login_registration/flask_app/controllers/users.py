from flask_app import app
from flask import render_template , request, redirect
from flask_app.models.user import User 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create', methods = ['POST'])
def create_user():
    if User.validate_register(request.form):
        User.create(request.form)
    print(request.form)
    return redirect('/')




