# get-weather.py installer v0.1 by maxrt101
# -*- coding: utf-8 -*-
import argparse

parser = argparse.ArgumentParser(description='get_weather.py installer')
parser.add_argument('-v', action='store_true', help='Display version and exit')
parser.add_argument('--cli', action='store_true', help='cli')
parser.add_argument('-a', action='store', dest='api_key', type=str,help='Api key', default='')
parser.add_argument('-c', action='store', dest='city',type=str, help='City', default='')
parser.add_argument('-cc', action='store', dest='country_code', type=str, help='Country Code', default='')
parser.add_argument('-u', action='store', dest='units', type=str, help='Units', default='metric')

args = parser.parse_args()

src = """# get-weather.py 1.0 by maxrt101
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
parser.add_argument('-a', action='store', dest='api_key', type=str,help='Api key', default='{}')
parser.add_argument('-c', action='store', dest='city',type=str, help='City', default='{}')
parser.add_argument('-cc', action='store', dest='country_code', type=str, help='Country Code', default='{}')
parser.add_argument('-u', action='store', dest='units', type=str, help='Units', default='{}')

args = parser.parse_args()

"""

def line_prepender(orig, filename, line):
	f1 = open(orig, 'r')
	content = f1.read()

	f = open(filename, 'w')
	f.write(line + '\n' + content)
	
	f1.close()
	f.close()

def cli():
	print("Enter your api key")
	print("Which you can obtain on https://openweathermap.org/, just sign up, it's free")
	api_key = raw_response(': ')
	print("Enter city name")
	print("If you live in small one, just use the name of nearest big city")
	city = raw_response(': ')
	print("Enter country code")
	country_code = raw_response(': ')
	print("Units (default metric)")
	print("Leave blank for Kelvin/ 'metric' for Celsius/ 'imperial' for Fahrenheit")
	units = raw_response(': ')
	
	print('Saving file...')
	line_prepender('src.py', 'get_weather.py', src.format(args.api_key, args.city, args.country_code, args.units))

	print('Done')

if args.cli:
	cli()
else:
	if (args.api_key == '') or (args.city == '') or (args.country_code == ''):
		print('ERROR: ')
		exit()
	line_prepender('src.py', 'get_weather.py', src.format(args.api_key, args.city, args.country_code, args.units))