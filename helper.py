from geopy.geocoders import Nominatim
#from bot import *
import bot
import random

def get_lat_long(city):
    geolocator = Nominatim(user_agent="discord python weather bot")
    location = geolocator.geocode(city)
    #print(location.longitude)
    lat = location.latitude
    lon = location.longitude
    return (lat,lon)

def fix_weather_degree_string(degree_string):
    return degree_string.replace("\u00b0", "°")

def flatten(lst):
    """
    Flattens a nested list into a single list.

    Args:
        lst (list): The list to be flattened. Can contain elements of any type, including lists.

    Returns:
        list: A flattened version of the input list, containing only non-list elements.
    """
    return [item for sublist in lst 
            for item in (flatten(sublist) 
            if isinstance(sublist, list) else [sublist])]

def command_string(string:str) -> str:
    """
    This function takes a string as input and returns the same string if it starts with an exclamation mark (!) or returns the string with an exclamation mark appended to the beginning of it.

    Args:
    string (str): The input string to be modified.

    Returns:
    str: The modified string.
    """
    return string if string.startswith("!") else f"!{string}"

def fix_command(strings:list) -> list[str]:
    """
    This function takes a list of strings as input and returns a new list of strings with any commands fixed. A string is considered to contain a command if it starts with an exclamation mark (!) or if an exclamation mark is appended to the beginning of the string.

    Args:
    strings (list): The list of strings to be fixed.

    Returns:
    list[str]: A new list of strings with any commands fixed.
    """
    return [command_string(string) for string in strings]

def random_greeting(name:str="<NAME>"):
    commands = bot.Commands()
    return random.choice(list(map(lambda word: f"{word[1:].capitalize()}, {name}!", commands.greets())))
