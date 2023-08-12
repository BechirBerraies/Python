from flask_app import app
from flask import render_template , request, redirect,session, flash
from flask_app.models.author import Author


from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)



@app.route('/')
def dashbord():
    all_authors = Author.get_all()
    return render_template("dashbord.html", all_authors = all_authors)

@app.route('/create/author', methods = ['POST'])
def create_author():
        
        Author.create(request.form)
        return redirect('/')

@app.route('/author/<int:id>')
def get_author():
    data
    Author.get_by_id()

