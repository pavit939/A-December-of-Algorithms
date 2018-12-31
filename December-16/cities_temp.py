import requests,json
api_key = "8af56c91890726fc507de74a7eee305b"
url = "http://api.openweathermap.org/data/2.5/weather?"
city1 = input("Enter city name 1:")
city2 = input("Enter city name 2:")
url1 = url + "appid=" + api_key + "&q=" + city1
url2 = url + "appid=" + api_key + "&q=" + city2
response1 = requests.get(url1)
response2 = requests.get(url2)
x1 = response1.json()
x2 = response2.json()
if x["cod"] != "404":
	y1 = x1["main"]
	currenttemp1 = y1["temp"]
	print("Temperature at",city1,"(kelvin) = " +
					str(currenttemp1) )
else:
	print(" City Not Found ")
if x2["cod"] != "404":
	y2 = x2["main"]
	currenttemp2 = y2["temp"]
	print("Temperature at", city2, "(kelvin) = " +
		  str(currenttemp2))
else:
	print(" City Not Found ")
print("Temperature difference between the cities is =",currenttemp1-currenttemp2)
