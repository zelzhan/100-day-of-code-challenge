from pprint import pprint as pp
import requests
import json

API_KEY = '764a6eef4e124abcacd110142183011'
API_URL = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=' + API_KEY + '&q={}&format=json&date={}' #city and date


def allyears(city, time):
	time = time.split("-")
	year = int(time[0])
	result = []
	while year != 2008:
		time[0] = str(year)
		unparsed = requests.get(API_URL.format(city, "-".join(time))).text #call for api
		parsed = json.loads(unparsed)
		mintemp = parsed['data']['weather'][0]['maxtempC']
		maxtemp = parsed['data']['weather'][0]['mintempC']
		cityFromApi = parsed['data']['request'][0]['query']
		hourlyTemp = parsed['data']['weather'][0]['hourly']
		average = 0
		for hourTemp in hourlyTemp:
			average += int(hourTemp['tempC'])
		average /= len(hourlyTemp)
		result.append({'mintemp':mintemp, 'maxtemp':maxtemp, 'average':average, 'city':cityFromApi, 'year':year})
		year-=1
	return result
		

def query(city, time):
	try:
		print(city)
		data = allyears(city, time)
		# data = {'mintemp':mintemp, 'maxtemp':maxtemp, 'average':average, 'city':cityFromApi}
	except Exception as e:
		pp(e)
		data = None
	return data