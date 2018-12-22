import json

def extract_day(time):
	months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06",
			 "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
	time = time.split()
	result = "{}-{}-{}".format(time[3], months[time[1]], time[2])

	return result

def jsonProcess(data):
	for i in range(len(data)):
		data[i] = data[i].replace("\'", "\"")
		data[i] = json.loads(data[i])
	print(data)
	return data