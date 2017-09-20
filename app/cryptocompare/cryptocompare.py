import json, requests

def listCoins():
    #https://www.cryptocompare.com/api/data/coinlist/
    r = requests.get('https://www.cryptocompare.com/api/data/coinlist/')
    response = json.loads(r.text)
    coins = [coin.encode('ascii','ignore') for coin in response["Data"]]
    return json.dumps(sorted(coins))

def tickerCoin():
    return
