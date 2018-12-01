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
		cityFromApi = parsed['data']['request'][0]['query']
		hourlyTemp = parsed['data']['weather'][0]['hourly']
		average = 0
		for hourTemp in hourlyTemp:
			average += int(hourTemp['tempC'])
		average /= len(hourlyTemp)
		data = {'mintemp':mintemp, 'maxtemp':maxtemp, 'average':average, 'city':cityFromApi}
	except Exception as e:
		pp(e)
		data = None
	return data
	