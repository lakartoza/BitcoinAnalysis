import requests

def get_json_from_market(CoinPairStr):
		r = requests.get('https://bittrex.com/api/v1.1/public/getmarkethistory?market='+CoinPairStr)
		return r.json()["result"]

