 #! /usr/bin/env python3
     
"""Non-comprehensive example of your code demonstrating some good
Python coding practices.
     
See https://www.python.org/dev/peps/pep-0008/
"""
     
import requests
     
     
__version__ = "0.1"
__license__ = "MIT"
__author__ = "Someone"
__credits__ = "rebirth, pomf"
     
     
def ctof(temp):
        """Convert temperature from Celsius to Fahrenheit."""
        return temp * 9/5 + 32  # functions should be surrounded by 2 blank lines
     
     
def main():
        api_key = "3b64cccda8b44210a213a00698a8028a"
        city = input("City name:")  # inline comments minimum 2 spaces after statement
        uri = f"https://api.weatherbit.io/v2.0/current?city={city}&key={api_key}"
        weather_data = requests.get(uri).json()
        ccode = weather_data["data"][0]["country_code"]
        sunrise = weather_data["data"][0]["sunrise"]
        clouds = weather_data["data"][0]["clouds"]
        wind_cdir = weather_data["data"][0]["wind_cdir"]
        wind_spd = weather_data["data"][0]["wind_spd"]
        uv = weather_data["data"][0]["uv"]
        sunset = weather_data["data"][0]["sunset"]
        datetime = weather_data["data"][0]["datetime"]
        celsius = weather_data["data"][0]["temp"]
        fahrenheit = f"{ctof(celsius):.1f}"  # truncate to only one decimal place
        conditions = weather_data["data"][0]["weather"]["description"]
     
        print(f"||Conditions: {conditions} - "
              f"||Temperature: {celsius} °C / {fahrenheit} °F "
	      f"||Country Code: {ccode}"
              f"||Sunrise: {sunrise}"
              f"||Sunset: {sunset}"
              f"||Datetime: {datetime}"
              f"||Clouds: {clouds}"
              f"||WindCdir: {wind_cdir}"
              f"||Wind_spd: {wind_spd}"
              f"||UV :{uv}"
              )
     
if __name__ == "__main__":
        main()
