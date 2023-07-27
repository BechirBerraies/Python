


from flask_app import app
from flask import render_template, redirect , request
from flask_app.models.dojo import Dojo


@app.route ('/')
def index ():
    all_dojos = Dojo.get_all()
    return render_template('index.html', all_dojos = all_dojos )

@app.route ('/dojo/create', methods =['POST'])
def dojo_create ():
    Dojo.create(request.form)
    return redirect('/')

@app.route('/dojo/<int:dojo_id>')
def show_dojo(dojo_id):
    showdojo = Dojo.get_one_by_id({'id': dojo_id})
    return render_template('show.html', showdojo = showdojo)