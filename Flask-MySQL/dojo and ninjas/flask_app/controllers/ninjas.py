
from flask_app import app
from flask import render_template, redirect , request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    all_dojos = Dojo.get_all()
    return render_template ('ninjas.html', all_dojos= all_dojos)

@app.route('/ninjas/create' , methods = ['post'])
def ninja_create():
    Ninja.create(request.form)
    return redirect(('/ninjas'))

