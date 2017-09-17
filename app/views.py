from app import app
from flask import request
from flask import render_template
import json

@app.route('/', methods = [ 'GET', 'POST'])
@app.route('/index', methods = [ 'GET', 'POST'])
def index():
	return 'hello'
	#return render_template('index.html', title='CoinSlack')

@app.route('/api')
def entry():
	return 'version'
