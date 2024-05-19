from settings.league import League
import json


class Settings:
    """
    A class representing user settings for managing starting year, ending year, and league.

    Attributes:
        starting_year (int): The starting year for data retrieval.
        ending_year (int): The ending year for data retrieval.
        league (League): The selected football league for data retrieval.
    """

    def __init__(self, starting_year: int, ending_year: int, league: League):
        """
        Initializes a Settings object with starting year, ending year, and league.

        Args:
            starting_year (int): The starting year for data retrieval.
            ending_year (int): The ending year for data retrieval.
            league (League): The selected football league for data retrieval.
        """
        self.starting_year = starting_year
        self.ending_year = ending_year
        self.league = league

    def __str__(self):
        """Returns a string representation of the Settings object"""
        return f"Starting Year: {self.starting_year}, Ending: {self.ending_year}, League: {self.league}"

    @classmethod
    def default(cls):
        """
        Returns the default settings.

        Returns:
            Settings: A Settings object with default values.
        """
        return cls(2010, 2024, League.E0)

    @classmethod
    def user(cls):
        """
        Returns the user-defined settings from a JSON file.

        Returns:
            Settings: A Settings object with user-defined values.
        """
        with open('settings/settings.json', 'r') as file:
            json_data = json.load(file)
            return cls(json_data["starting_year"], json_data["ending_year"], League[json_data["league"]])

    def update_attribute(self, attribute_name: str, value: any):
        """
        Updates the value of a specific attribute.

        Args:
            attribute_name (str): The name of the attribute to be updated.
            value (any): The new value for the attribute.

        Raises:
            AttributeError: If the specified attribute does not exist.
        """
        if hasattr(self, attribute_name):
            setattr(self, attribute_name, value)
        else:
            raise AttributeError(f"'Settings' object has no attribute '{attribute_name}'")

    def to_dict(self) -> dict[str: any]:
        """
        Converts the Settings object to a dictionary.

        Returns:
            dict[str, any]: A dictionary containing the settings attributes.
        """
        return {"league": self.league.name, "starting_year": self.starting_year, "ending_year": self.ending_year}
