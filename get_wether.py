# get-weather.py 1.0 by maxrt101
# -*- coding: utf-8 -*-
import sys
import json
import urllib2
import argparse
from datetime import datetime
from datetime import timedelta

parser = argparse.ArgumentParser(description='get_weather.py')
parser.add_argument('-v', action='store_true', help='Display version and exit')
parser.add_argument('-sr', action='store_true', help='Show http response')
parser.add_argument('-a', action='store', dest='api_key', type=str,help='Api key', default='')              # You can obtain it on https://openweathermap.org/, just sign up, it's free
parser.add_argument('-c', action='store', dest='city',type=str, help='City', default='')                    # Your city name 
parser.add_argument('-cc', action='store', dest='country_code', type=str, help='Country Code', default='')  # Cointry code (US, UK)
parser.add_argument('-u', action='store', dest='units', type=str, help='Units', default='metric')           # Leave blank for Kelvin/ 'metric' for Celsius/ 'imperial' for Fahrenheit

args = parser.parse_args()

version = '1.0'

colors = {
	"white": '\033[0m',
	"green": '\033[32m',
	"yellow": '\033[33m',
	"blue": '\033[34m',
	"cyan": '\033[36m',
	"gray": '\033[90m' #37m
}

thunder = [200 , 201 , 202 , 210 , 211 , 212 , 221 , 230 , 231 , 232 ]
drizzle = [300 , 301 , 302 , 310 , 311 , 312 , 313 , 314 , 321 , 500 , 501 , 502 ]
rain = [503 , 504 , 520 , 521 , 522 , 531 ]
lightsnow = [600 , 601 ]
heavysnow = [602 , 622 ]
snowandrain = [611 , 612 , 615 , 616 , 620 , 621 ]
atmosphere = [701 , 711 , 721 , 731 , 741 , 751 , 761 , 762 , 771 , 781 ]
clear = 800
partlycloudy = [801 , 802 , 803 ]
cloudy = 804
windy = [900 , 901 , 902 , 903 , 904 , 905 , 906 , 951 , 952 , 953 , 954 , 955 , 956 , 957 , 958 , 959 , 960 , 961 , 962 ]

def deg_convert(d):
	if d == 'NONE':
		return d

	dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
	ix = int((d + 11.25)/22.5)
	return dirs[ix % 16]


def get_weather(api_key, city_name, country_name, units):
	# GET request	
	raw_response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q={},{}&units={}&appid={}&type=accurate&mode=json'.format(city_name, country_name, units, api_key))
	json_response = raw_response.read()

	#json-parse
	response = json.loads(json_response)

	if args.sr:
		print(json_response)
	
	city = response["name"]
	time = (datetime.utcfromtimestamp(response["dt"]) + timedelta(hours=3)).strftime('%H:%M:%S')
	sunrise_time = (datetime.utcfromtimestamp(response["sys"]["sunrise"]) + timedelta(hours=3)).strftime('%H:%M:%S')
	sunset_time = (datetime.utcfromtimestamp(response["sys"]["sunset"]) + timedelta(hours=3)).strftime('%H:%M:%S')
	temperature = response["main"]["temp"]
	humidity = response["main"]["humidity"]
	temp_min = response["main"]["temp_min"]
	temp_max = response["main"]["temp_max"]
	wind_speed = response["wind"]["speed"]
	try:
		wind_direction = response["wind"]["deg"]
	except:
		wind_direction = 'NONE'
	clouds = response["clouds"]["all"]
	weather_condition = int(response["weather"][0]["id"])
	weather_main_description = response["weather"][0]["main"]
	weather_description = response["weather"][0]["description"]
	
	weather = 'Current weather: ' + weather_description
	current_temp = "Current Temp: " + str(temperature) +  " °C"
	high = "Today's High: " + str(temp_max) +  " °C"
	low = "Today's Low: " + str(temp_min) +  " °C"
	humidity = "Humidity: " + str(humidity) + '%'
	wind_info = "Wind speed: " + str(wind_speed) + "m/s - Direction: " + deg_convert(wind_direction)
	clouds_info = "Clouds: " + str(clouds) + "%"
	sunrise = "Sunrise: " + str(sunrise_time)
	sunset = "Sunset: " + str(sunset_time)
	
	space_1 = 40 - len(weather)
	
	str1 = colors["white"] + weather + (' ' * space_1) + humidity
	str2 = colors["white"] + current_temp + '			' + ""
	str3 = colors["white"] + high + '			' + wind_info
	str4 = colors["white"] + low + '			' + clouds_info
	str5 = colors["white"] + sunrise + '			' + sunset

	#OUTPUT
	print("")
	print("Current weather conditions for {}".format(city))
	print("")
	
	if (weather_condition in thunder):
		print(colors["gray"] +  "	    .--.   		" + colors["white"] + str1)
		print(colors["gray"] +  "	 .-(    ). 		" + colors["white"] + str2)
		print(colors["gray"] +  "	(___.__)__)		" + colors["white"] + str3)
		print(colors["yellow"] +"	  /_   /_  		" + colors["white"] + str4)
		print(colors["yellow"] +"	   /    /  		" + colors["white"] + str5)
		print("")

	elif (weather_condition in drizzle):
		print(colors["gray"] +"	  .-.   		" + colors["white"] + str1)
		print(colors["gray"] +"	 (   ). 		" + colors["white"] + str2)
		print(colors["gray"] +"	(___(__)		" + colors["white"] + str3)
		print(colors["cyan"] +"	 / / / 			" + colors["white"] + str4)
		print(colors["cyan"] +"	  /  			" + colors["white"] + str5)
		print("")
	
	elif (weather_condition in rain):
		print(colors["gray"] +"	    .-.   		" + colors["white"] + str1)
		print(colors["gray"] +"	   (   ). 		" + colors["white"] + str2)
		print(colors["gray"] +"	  (___(__)		" + colors["white"] + str3)
		print(colors["cyan"] +"	 //////// 		" + colors["white"] + str4)
		print(colors["cyan"] +"	 /////// 		" + colors["white"] + str5)
		print("")
	elif (weather_condition in lightsnow):
		print(colors["gray"] + "	  .-.   		" + colors["white"] + str1)
		print(colors["gray"] + "	 (   ). 		" + colors["white"] + str2)
		print(colors["gray"] + "	(___(__)		" + colors["white"] + str3)
		print(colors["white"] +"	 *  *  *		" + str4)
		print(colors["white"] +"	*  *  * 		" + str5)
		print("")
	elif (weather_condition in heavysnow):
		print(colors["gray"] + "	    .-.   		" + colors["white"] + str1)
		print(colors["gray"] + "	   (   ). 		" + colors["white"] + str2)
		print(colors["gray"] + "	  (___(__)		" + colors["white"] + str3)
		print(colors["white"] +"	  * * * * 		" + str4)
		print(colors["white"] +"	 * * * *  		" + str5)
		print(colors["white"] +"	  * * * *       ")
		print("")
	elif (weather_condition in snowandrain):
		print(colors["gray"] + "	  .-.   		" + colors["white"] + str1) 
		print(colors["gray"] + "	 (   ). 		" + colors["white"] + str2)
		print(colors["gray"] + "	(___(__)		" + colors["white"] + str3)
		print(colors["white"] + "	 *" + colors["cyan"] + "/ " + colors["white"] + "*" + colors["cyan"] + "/" + colors["cyan"] + "*" + str4)
		print(colors["white"]+ "	* " + colors["cyan"] + "/" + colors["white"] + "* " + colors["cyan"] + "/" + colors["white"] + "*" + str5)
		print("")
	elif (weather_condition in atmosphere):
		print(colors["gray"] + "	_ - _ - _ -		" + colors["white"] + str1)
		print(colors["gray"] + "	 _ - _ - _ 		" + colors["white"] + str2)
		print(colors["gray"] + "	_ - _ - _ -		" + colors["white"] + str3)
		print(colors["gray"] + "	 _ - _ - _ 		" + colors["white"] + str4)
		print("				" + str5)
		print("")
	elif ((weather_condition == clear) and (time > "18:00:00" or time < "05:00:00") ):
		print("	    *  --.			" + str1)
		print("	        \  \   *		" + str2)
		print("	         )  |    *		" + str3)
		print("	*       <   |			" + str4)
		print("	   *    ./ /	  		" + str5)
		print("	       ---'   *   ")
		print("")
	elif ( weather_condition == clear):
		print(colors["yellow"] + "	   \ | /  		" + colors["white"] + str1) 
		print(colors["yellow"] + "	    .-.   		" + colors["white"] + str2)
		print(colors["yellow"] + "	-- (   ) --		" + colors["white"] + str3)
		print(colors["yellow"] + "	    ``'``   		" + colors["white"] + str4)
		print(colors["yellow"] + "	   / | \  		" + colors["white"] + str5)
		print("")
	elif ( weather_condition in partlycloudy):
		print(colors["yellow"] + "	   \ | /   		"+ colors["white"] + str1) 
		print(colors["yellow"] + "	    .-.    		"+ colors["white"] + str2)
		print(colors["yellow"] + "	-- ( "+ colors["white"] +" .--. 		" + str3)  
		print("	   .-(    ). 		" + str4)
		print("	  (___.__)__)		" + str5)
		print("")
	elif ( weather_condition == cloudy):
		print("	    .--.   		" + str1)
		print("	 .-(    ). 		" + str2)
		print("	(___.__)__)		" + str3)
		print("	            		" + str4)
		print("				" + str5)
		print("")
	elif ( weather_condition in windy ):
		print("	~~~~      .--.   		" + str1)
		print("	 ~~~~~ .-(    ). 		" + str2)
		print("	~~~~~ (___.__)__)		" + str3)
		print("	                 		" + str4)
		print("					" + str5)
	else:
		print("ERROR: invalid weather id")

if args.v:
	print('get_weather v{} (c)2019 maxrt101'.format(version))
else:
	if (args.api_key == '') or (args.city == '') or (args.country_code == ''):
		print('ERROR: make sure that api key, city and country code is pesent')
		print('You can either run install.py under installer/, or manually insert values in this script')
		exit()
	else:
		get_weather(args.api_key, args.city, args.country_code, args.units)