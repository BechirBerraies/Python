from flask import Flask, render_template,redirect,session,request
app = Flask(__name__)

app.secret_key = 'afafa'
@app.route('/')          
def hello_world():
    return render_template('index.html') 


@app.route('/process', methods = ['POST'])
def process():
    session['name']= request.form['name']
    session['location']= request.form['location']
    session['language']= request.form['language']
    session['comment']= request.form['comment']
    return redirect('display')

@app.route('/display')
def display():
    return render_template('display.html')





if __name__=="__main__":     
    app.run(debug=True)
