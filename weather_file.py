# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
This module provides a class for retrieving and formatting weather data for a given city.

Attributes:
---
    city (str): The name of the city for which to retrieve weather data. Defaults to "esbjerg".
    api_key (str): The API key used to access the OpenWeatherMap API.

Methods:
---
    weather: Retrieves and returns current weather data for the specified city as a formatted string.
"""
import os
import requests
from dotenv import load_dotenv
import helper
load_dotenv()


class Weather:
    """
    A class for accessing weather information.

    Attributes:
    ---
        city (str): The city for which to retrieve weather information.
        api_key (str): The API key for accessing OpenWeatherMap's API.

    Methods:
    ---
        weather: Returns a string containing weather information for the specified city.
    """
    def __init__(self, city: str = "esbjerg") -> None:
        self.city = city
        self.api_key = os.getenv("openWeather_API_KEY")
    def weather(self):
        """
        Retrieves weather information for a given city.

        Args:
        ---
            none
        Returns:
        ---
            str: A string containing weather information for the specified city, including:\n
                - current temperature
                - humidity
                - wind speed.
            If the city could not be found, returns an error message.
        """
        celsius = "°"
        try:
            lat, lon = helper.get_lat_long(self.city)
        except AttributeError:
            return f"Im sorry. I could not find the city \"{self.city}\"\nIf this is an bug, please contact **Tr4shL0rd#8279** or create a new issue on https://github.com/Tr4shL0rd/Tr4shBot/issues" #pylint:disable=line-too-long
        resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}&units=metric", timeout=1).json() #pylint:disable=line-too-long
        sky_desc        = resp["weather"][0]["main"]
        actual_temp     = int(resp["main"]["temp"])
        feels_like_temp = int(resp["main"]["feels_like"])
        humidity        = resp["main"]["humidity"]
        wind_speeds     = resp["wind"]["speed"]
        return f"""
In {self.city.title()}
it's currently {actual_temp}{celsius}C and feels like {feels_like_temp}{celsius}C.
It's currently {sky_desc.lower()} outside right now, with a humidity of {humidity}% and the wind is blowing at speeds of {wind_speeds} m/s.
"""
