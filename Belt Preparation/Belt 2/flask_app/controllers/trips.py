from flask_app import app
from flask import render_template , request, redirect,session, flash, url_for
from flask_app.models.trip import  Trip
from flask_app.models.user import User 





@app.route('/dashbord')
def dashbord():
    if 'user_id' not in session:
        return redirect('/')
    logged_user = User.get_by_id({'id':session['user_id']})
    all_trips = Trip.get_all({'id':session['user_id']})
    return render_template("dashbord.html", user = logged_user, all_trips = all_trips)

@app.route('/trips/new')
def trip_new():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('new_trip.html')

@app.route('/trips/create', methods= ['POST'])
def create_trip():
    print("**************"*20,request.form)
    if Trip.validate_trip(request.form):
        data ={
            **request.form,
            'user_id':session['user_id']
        }
        Trip.create(data)
        return redirect('/dashbord')
    return redirect('/trips/new')

@app.route('/trips/edit/<int:id>')
def edit_trip(id):
    if 'user_id' not in session:
        return redirect('/')
    trip = Trip.get_by_id({'id':id})
    return render_template("edit.html" ,trip= trip)


@app.route('/trips/update/<int:id>', methods=['POST'])
def update_recipe(id):
    print("**************"*20,request.form)
    if Trip.validate_trip(request.form):
        print(request.form)
        data ={
            **request.form,
            'id':id
        }
        print("+"*20,data,"*"*20)
        Trip.edit_trip(data)
        return redirect('/dashbord')
    return redirect(url_for('edit_trip', id=id))


@app.route('/delete/<int:id>', methods = ['post'])
def delete(id):
    if 'user_id' not in session:
        return redirect('/')
    Trip.delete_trip({'id':id})
    return redirect('/dashbord')

@app.route('/trips/<int:id>')
def view_trip(id):
    if 'user_id' not in session:
        return redirect('/')
    trip = Trip.get_by_id({'id':id})
    logged = User.get_by_id({'id':session['user_id']})
    return render_template("view.html", trip = trip , logged =logged)