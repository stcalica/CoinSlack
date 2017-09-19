from app import app
from flask import request
from flask import render_template
import json, requests

@app.route('/', methods = [ 'GET', 'POST'])
@app.route('/index', methods = [ 'GET', 'POST'])
def index():
	return 'hello'
	#return render_template('index.html', title='CoinSlack')

@app.route('/api')
def entry():
	return 'version'


@app.route('/coins')
def coinList():
	#https://www.cryptocompare.com/api/data/coinlist/
	r = requests.get('https://www.cryptocompare.com/api/data/coinlist/')
	data = json.loads(r.text)
	coins = data["Data"]
	print(type(json.loads(coins)))
	return json.dumps(coins)
