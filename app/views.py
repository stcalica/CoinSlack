from app import app
from flask import request
from flask import render_template
from flask import jsonify
import json, requests

@app.route('/', methods = [ 'GET', 'POST'])
@app.route('/index', methods = [ 'GET', 'POST'])
def index():
	print(request.data)
	return 'hello'
	#return render_template('index.html', title='CoinSlack')

@app.route('/api')
def entry():
	return 'version'


@app.route('/coins', methods = [ 'GET', 'POST'])
def coinList():
	#https://www.cryptocompare.com/api/data/coinlist/
	r = requests.get('https://www.cryptocompare.com/api/data/coinlist/')
	response = json.loads(r.text)
	coin_data = response["Data"] #dictionary
	coins = [coin for coin in response["Data"]]
	return jsonify(coins) 
