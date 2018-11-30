from pprint import pprint as pp
import requests
import json

API_KEY = '764a6eef4e124abcacd110142183011'
API_URL = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=' + API_KEY + '&q={}&format=json&date={}' #city and date



def query(city):
	try:
		print(city)
		unparsed = requests.get(API_URL.format(city, '2018-11-30')).text #call for api
		parsed = json.loads(unparsed)
		mintemp = parsed['data']['weather'][0]['maxtempC']
		maxtemp = parsed['data']['weather'][0]['mintempC']

		pp(parsed)

	except Exception as e:
		print(e)
		return str("cant")
		data = None
	print(city)
	