# Get weather python  
Python version of obs0letes [Get-Weather](https://github.com/obs0lete/Get-Weather)  
  
In order to work, this script needs Openwheathersmap's **Api Key**. **With out it, script will not work!**  
You can get yours at  https://openweathermap.org/, just sign up, and find Api Keys button.

### Installation  
1.[Download](https://github.com/maxrt101/get_weather/archive/master.zip) or [clone](https://github.com/maxrt101/get_weather) get weather.  
2.Make sure you have **python 2.7** and theese installed (usually theese packages are preinstalled):  
 - sys  
 - json  
 - urllib2  
 - argparse  
 - datetime  
 
3. Run `Installer/install.py` or manually insert values in `get_weather.py`. Requested values are:
 - **Api Key**
 - **City name**
 - **Country code**
 - **Units**
 
 4. Run `get_weather.py` (See Usage)

### Usage
`Usage: get_wether_dev.py [-h] [-v] [-sr] [-a API_KEY] [-c CITY] [-cc COUNTRY_CODE] [-u UNITS]`  

#### Arguments:  
**-h** - Help. Display help message and exit  
**-v** - Version. Display version and exit  
**-sr** - Show http response  
**-a API_KEY** - Api Key. You can obtain it on https://openweathermap.org/, just sign up, it's free  
**-c CITY** - City name  
**-cc COUNTRY_CODE** - Country code  
**-u UNITS** - Units. Leave blank for Kelvin/ 'metric' for Celsius/ 'imperial' for Fahrenheit  
