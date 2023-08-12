from flask_app import app
from flask import render_template , request, redirect,session, flash, url_for
from flask_app.models.book import  Book
from flask_app.models.user import User 



@app.route('/book/new')
def new_book():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("newbooks.html")

@app.route('/book/create', methods= ['POST'])
def create_recipe():
    print("**************"*20,request.form)
    if Book.validate_recipe(request.form):
        data ={
            **request.form,
            'user_id':session['user_id']
        }
        Book.create(data)
        return redirect('/dashbord')
    return redirect('/book/new')
