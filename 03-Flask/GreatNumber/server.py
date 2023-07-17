import random 
from flask import Flask, render_template,session, redirect
app = Flask(__name__)

app.secret_key = 'adaafa'
@app.route('/')          
def hello_world():
    return render_template('index.html')

@app.route('/therandom')
def therandom():
    session['number'] = random.randint(1, 100)
    return redirect('/')

@app.route ('/process', methods = ['POST'])
def process():
    print("*"*20,session['randy'],"*"*20)
    return redirect('/')


if __name__=="__main__":     
    app.run(debug=True)    


def thefunction():
    print(random.randint(1, 100))