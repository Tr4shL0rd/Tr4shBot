import requests

class DogFact:
    """
    This class is used to retrieve random dog facts from an online API.

    Attributes:
    None

    Methods:
    random_fact: Returns a random dog fact as a string.
    """
    def __init__(self) -> None:
        """
        The constructor for the DogFact class.

        Args:
        None

        Returns:
        None
        """
        pass
    def random_fact(self) -> str:
        """
        Retrieves a random dog fact from an online API and returns it as a string.

        Args:
        None

        Returns:
        str: A random dog fact.
        """
        return requests.get("https://dogapi.dog/api/facts").json()["facts"][0]


class CatFact:
    """
    This class is used to retrieve random cat facts from an online API.

    Attributes:
    None

    Methods:
    random_fact: Returns a random cat fact as a string.
    """

    def __init__(self) -> None:
        """
        The constructor for the CatFact class.

        Args:
        None

        Returns:
        None
        """
        pass

    def random_fact(self) -> str:
        """
        Retrieves a random cat fact from an online API and returns it as a string.

        Args:
        None

        Returns:
        str: A random cat fact.
        """
        return requests.get("https://meowfacts.herokuapp.com/").json()["data"][0]