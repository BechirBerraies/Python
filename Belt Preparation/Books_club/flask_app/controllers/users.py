from flask_app import app
from flask import render_template , request, redirect,session, flash
from flask_app.models.user import User 
from flask_app.models.book import Book 


from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route('/recipes')
def dashbord():
    if 'user_id' not in session:
        return redirect('/')
    logged_user = User.get_by_id({'id':session['user_id']})
    all_recipes = User.get_all()
    return render_template("recipes.html",user = logged_user, all_recipes = all_recipes)