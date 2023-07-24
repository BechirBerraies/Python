from flask import Flask, render_template,redirect,request

from artist_model import Artist

app = Flask(__name__)
@app.route('/')
def dashbord():
    all_artists = Artist.get_all()
    print(all_artists)
    return render_template('dashbord.html', artists = all_artists)

@app.route('/artists/new')
def new_artists():
    return render_template('new_artist.html')

@app.route('/artists/create' , methods = ['POST'])
def create_artist():
    print("*"*20,request.form)
    
    data_dict = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'nationality':request.form['nationality'],
        'rate':request.form['rate'],
        'image':request.form['image'],
    }
    
    if 'is_dead' in data_dict:
        data_dict['is_dead']= 1 
    else:
        data_dict['is_dead']= 0 
    
    Artist.create_artist(data_dict)


    return redirect('/')

@app.route('/artists/<int:artist_id>')
def viewartist(artist_id):
    data_dict = {'id':artist_id}
    artist = Artist.get_one_by_id(data_dict)

    return render_template('show_artist.html', artist = artist )



@app.route('/artists/<int:artist_id>/edit')
def edit(artist_id):
    return render_template('edit.artist.html')



@app.route('/artists/<int:artist_id>/delete')
def delete(artist_id):
    data_dict = {'id': artist_id}
    artist = Artist.delete(data_dict)
    return redirect('/')



    


if __name__ == '__main__':
    app.run(debug=True,port=5001)