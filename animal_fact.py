# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
This module consists of two classes, DogFact and CatFact, that are used to retrieve
random facts about dogs and cats, respectively, from online APIs.

Attributes:
---
    None

Methods:
---
    random_fact: Retrieves a random fact from an online API and returns it as a string.
"""
import requests


class DogFact:
    """
    This class is used to retrieve random dog facts from an online API.

    Attributes:
    ---
        None

    Methods:
    ---
        random_fact: Returns a random dog fact as a string.
    """

    def __init__(self) -> None:
        """
        The constructor for the DogFact class.

        Args:
        ---
            None

        Returns:
        ---
            None
        """

    def random_fact(self) -> str:
        """
        Retrieves a random dog fact from an online API and returns it as a string.

        Args:
        ---
            None

        Returns:
        ---
            str: A random dog fact.
        """
        return requests.get("https://dogapi.dog/api/facts", timeout=1).json()["facts"][
            0
        ]


class CatFact:
    """
    This class is used to retrieve random cat facts from an online API.

    Attributes:
    ---
        None

    Methods:
    ---
        random_fact: Returns a random cat fact as a string.
    """

    def __init__(self) -> None:
        """
        The constructor for the CatFact class.

        Args:
        ---
            None

        Returns:
        ---
            None
        """

    def random_fact(self) -> str:
        """
        Retrieves a random cat fact from an online API and returns it as a string.

        Args:
        ---
            None

        Returns:
        ---
            str: A random cat fact.
        """
        return requests.get("https://meowfacts.herokuapp.com/", timeout=1).json()[
            "data"
        ][0]
