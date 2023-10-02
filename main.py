# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/cow')
def cow():
    return 'MOoooOo!'

@app.route('/final')
def final():
    return 'Welcome to my final assignment!'

@app.route('/pass')
def passit():
    return 'I hope I will pass for the first time ^^'
