from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def hello():
	user = {'username': "miguel"}
	return render_template('index.html', title="grigory",user=user)