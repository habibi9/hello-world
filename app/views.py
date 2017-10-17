from flask import render_template, request
from app import app

@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html')

@app.route('/receive', methods = ['POST', 'GET'])
def receive():
	if request.method == 'POST':
		name = request.form['name']
		age = request.form['age']
		year = str(2017 - int(age))
		return "Your name is " + name + ", and you were born in " + year
	if request.method == 'GET':
		return "This is a message from the server."
	
