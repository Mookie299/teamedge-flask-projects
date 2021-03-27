from flask import Flask, render_template, request, current_app as app 
from sense_hat import SenseHat
from time import sleep

sense = SenseHat ()

app = Flask(__name__)
#yerrrrrr
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success',methods=['POST'])
def sucess():
    message = request.form['message']
    sense.show_message(message)
    return render_template("success.html",message = message)
    
if __name__ == '__main__':
    app.run(debug = True, host ='0.0.0.0')