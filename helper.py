# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
This module provides several utility functions for a Discord bot.

Attributes:
---
    None

Methods:
---
    - get_lat_long: Returns the latitude and longitude for a given city.
    - flatten: Flattens a nested list into a single list.
    - command_string: Modifies a string to start with an exclamation mark (!)
        if it does not already start with one.
    - fix_command: Modifies a list of strings to start with an exclamation mark (!)
        if they do not already start with one.
    - random_greeting: Returns a random greeting with a specified name.
"""
from typing import Tuple
import random
from geopy.geocoders import Nominatim
import bot


def get_lat_long(city: str) -> Tuple[float, float]:
    """
    Returns the latitude and longitude for the specified city.

    Args:
    ---
        city: The name of the city.

    Returns:
    ---
        Tuple[float, float]: A tuple containing the latitude and longitude for the city.
    """
    geolocator = Nominatim(user_agent="discord python weather bot")
    location = geolocator.geocode(city)
    lat = location.latitude
    lon = location.longitude
    return (lat, lon)


def flatten(lst: list[list[object]]) -> list[object]:
    """
    Flattens a nested list into a single list.

    Args:
    ---
        - lst (List[List[object]]): The list to be flattened.
        Must contain elements of type `List[object]`, where `object` can be any type.

    Returns:
    ---
        List[object]: A flattened version of the input list, containing only non-list elements.
    """
    return [
        item
        for sublist in lst
        for item in (flatten(sublist) if isinstance(sublist, list) else [sublist])
    ]


def command_string(string: str) -> str:
    """
    This function takes a string as input and returns the same string if
    it starts with an exclamation mark (!) or returns the string with an exclamation
    mark appended to the beginning of it.

    Args:
    ---
        string (str): The input string to be modified.

    Returns:
    ---
        str: The modified string.
    """
    return string if string.startswith("!") else f"!{string}"


def fix_command(strings: list) -> list[str]:
    """
    This function takes a list of strings as input and returns a new
    list of strings with any commands fixed. A string is considered to contain a
    command if it starts with an exclamation mark (!) or if an exclamation mark
    is appended to the beginning of the string.

    Args:
    ---
        strings (list): The list of strings to be fixed.

    Returns:
    ---
        list[str]: A new list of strings with any commands fixed.
    """
    return [command_string(string) for string in strings]


def random_greeting(name: str = "<NAME>") -> str:
    """
    Returns a random greeting with the specified name.

    Args:
    ---
        name: The name to use in the greeting. Defaults to "<NAME>".

    Returns:
    ---
        str: A random greeting with the specified name.
    """
    commands = bot.Commands()
    greetings = list(
        set(
            commands.greets()
            + [
                "How's it going?",
                "How are ya?",
                "How's it hangin'?",
                "what's up?",
                "good'ay",
            ]
        )
    )
    return random.choice(
        list(
            map(
                lambda word: f"{word[1:].capitalize()}, {name.capitalize()}!"
                if word.startswith("!")
                else f"{word.capitalize()}, {name.capitalize()}!",
                greetings,
            )
        )
    ).capitalize()
