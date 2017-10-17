from flask import render_template, request
from app import app

@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html')

@app.route('/receive', methods = ['POST', 'GET'])
def receive():
	firstname = request.form['firstname']
	return firstname
	