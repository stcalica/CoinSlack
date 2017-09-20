from app import app
from flask import request
from flask import render_template
from flask import jsonify
from cryptocompare import cryptocompare as cc
import json, requests

@app.route('/', methods = [ 'GET', 'POST'])
@app.route('/index', methods = [ 'GET', 'POST'])
def index():
	
	return request.data

@app.route('/coins', methods = [ 'GET', 'POST'])
def coinList():
	return cc.listCoins()
