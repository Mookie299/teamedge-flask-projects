from flask import Flask, render_template, request, current_app as app 
from sense_hat import SenseHat
from time import sleep

sense = SenseHat ()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sucess',methods=['GET','POST'])
def sucess():
    message = request.form['message'] 
    return render_template("sucess.html",message = message)
    sense.show_message(message)

    
if __name__ == '__main__':
    app.run(debug = True, host ='0.0.0.0')