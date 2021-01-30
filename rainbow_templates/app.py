from flask import Flask, render_template, current_app as app

app = Flask(__name__)

@app.route('/')
def index():
    return  "Welcome to Daniella’s Rainbow Project"

@app.route('/red')
def rojo():
    color = 'red'
    return render_template('index.html',color = color)
@app.route('/orange')
def naranja():
    color = 'orange'
    return render_template('index.html', color = color)
@app.route('/yellow')
def amarillo():
    color = 'yellow'
    return render_template('index.html', color = color)
@app.route('/green')
def verde():
    color = 'green'
    return render_template('index.html', color = color)
@app.route('/blue')
def azul():
    color = 'blue'
    return render_template('index.html', color = color)
@app.route('/indigo')
def morado():
    color = 'indigo'
    return render_template('index.html', color = color)
@app.route('/violet')
def purple():
    color = 'violet'
    return render_template('index.html', color = color)
@app.route('/rainbow')
def rainbow():
    rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    return render_template('rainbow.html',rainbow = rainbow)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

