from flask import Flask, render_template,redirect,request

app = Flask(__name__)
@app.route('/')
def dashbord():
    return render_template('dashbord.html')



if __name__ == '__main__':
    app.run(debug=True,port=5001)