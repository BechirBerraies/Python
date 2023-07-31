from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo


app.secret_key = 'hey'

@app.route('/')          
def hello_world():
    return render_template('index.html') 


@app.route('/dojos/create', methods = ['POST'])
def create():
    if not Dojo.validate_Dojo(request.form):
        return redirect('/')
    id = Dojo.create(request.form)
    
    return redirect(f'/display/{id}')


@app.route('/display/<int:id>')
def display(id):
    dojo_id = {
        "id": id
    }
    dojo = Dojo.show_by_id(dojo_id)

    return render_template('display.html', dojo=dojo)




