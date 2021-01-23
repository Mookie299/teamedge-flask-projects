from flask import Flask, render_template, current_app as app

app = Flask(__name__)

@app.route('/')
def index():
    return  "Welcome to Daniella’s Rainbow Project"

@app.route('/red')
def rojo():
    return render_template('red.html')
@app.route('/orange')
def naranja():
    return render_template('orange.html')
@app.route('/yellow')
def amarillo():
    return render_template('yellow.html')
@app.route('/green')
def verde():
    return render_template('green.html')
@app.route('/blue')
def azul():
    return render_template('blue.html')
@app.route('/indigo')
def morado():
    return render_template('indigo.html')
@app.route('/violet')
def purple():
    return render_template('violet.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
