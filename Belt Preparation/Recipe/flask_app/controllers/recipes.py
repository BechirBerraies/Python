from flask_app import app
from flask import render_template , request, redirect,session, flash, url_for
from flask_app.models.recipe import  Recipe
from flask_app.models.user import User 




@app.route('/recipes')
def dashbord():
    if 'user_id' not in session:
        return redirect('/')
    logged_user = User.get_by_id({'id':session['user_id']})
    all_recipes = Recipe.get_all()
    return render_template("recipes.html",user = logged_user, all_recipes = all_recipes)

@app.route('/recipes/create', methods= ['POST'])
def create_recipe():
    print("**************"*20,request.form)
    if Recipe.validate_recipe(request.form):
        data ={
            **request.form,
            'user_id':session['user_id']
        }
        Recipe.create(data)
        return redirect('/recipes')
    return redirect('/recipes/new')


@app.route('/recipes/new')
def recipe_new():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('recipes_new.html')


@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({'id':id})
    return render_template("edit.html" ,recipe= recipe)


@app.route('/recipes/update/<int:id>', methods=['POST'])
def update_recipe(id):
    print("**************"*20,request.form)
    if Recipe.validate_recipe(request.form):
        print(request.form)
        data ={
            **request.form,
            'id':id
        }
        print("+"*20,data,"*"*20)
        Recipe.edit_recipe(data)
        return redirect('/recipes')
    return redirect(url_for('edit_recipe', id=id))


@app.route('/delete/<int:id>', methods = ['post'])
def delete(id):
    if 'user_id' not in session:
        return redirect('/')
    Recipe.delete_recipe({'id':id})
    return redirect('/recipes')

@app.route('/recipe/<int:id>')
def view_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({'id':id})
    logged = User.get_by_id({'id':session['user_id']})
    return render_template("view.html", recipe = recipe , logged =logged)