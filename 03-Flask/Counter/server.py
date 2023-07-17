from flask import Flask , render_template, session, redirect


app = Flask(__name__)
app.secret_key = "hdvhdvhczchzvhv"

@app.route('/')          
def hello_world(): 
    if 'count' not in session:
        session['count']=1
    return render_template('index.html')



@app.route('/count')
def count():
   session['count'] = session['count']+ 1
   print(session['count'])
   return redirect('/')

@app.route('/destroysession')
def reset():
    session.pop('count')
    return redirect('/')



if __name__=="__main__":   
    app.run(debug=True)    

