from flask import Flask, render_template , session , redirect  
app = Flask(__name__) 

app.secret_key = 'Lambadouza'

@app.route('/')     
def hello_world():
    return render_template('index.html')


@app.route('/process_money', methods = ['POST'])
def process_money():
        number = 3
        
        session['gold'] += number
        session['text'] += str(f"you gained {number} gold\n")


        return redirect('/')


@app.route('/reset', methods = ['POST'])
def reset():
    session['gold'] =0
    session['text']= str("")
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)   