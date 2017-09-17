from app import app
from flask import request
from flask import render_template
import json

@app.route('/')
@app.route('/index')
def index():
	return 'hello'
	#return render_template('index.html', title='CoinSlack')

@app.route('/api')
def entry():
	return 'version'
