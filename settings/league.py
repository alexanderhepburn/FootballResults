from enum import Enum


class League(Enum):
    """
    Enum class to represent various football leagues.
    Each enum member has a corresponding string representation for the league name.
    """

    E0 = "Premier League"
    E1 = "Championship"
    D1 = "Bundesliga 1"
    D2 = "Bundesliga 2"

    def __str__(self):
        """
        Returns the string representation of the league.
        """
        return self.value

    @classmethod
    def from_string(cls, value):
        """
        Converts a string to the corresponding League enum member.

        Args:
            value (str): The string representation of the league enum member.

        Returns:
            League: The corresponding League enum member.

        Raises:
            ValueError: If the input string does not match any enum member.
        """
        for league in cls:
            if league.name == value:
                return league
        raise ValueError(f"No such league: {value}")
