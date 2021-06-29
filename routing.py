from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def hello_name(name):
    return f"Hi, {name}!"

@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    return  int(num) * word

@app.route('/<this>')
def anything(this):
    return "Sorry! No response. Try again."

if __name__ == "__main__":  

    app.run(debug=True)
