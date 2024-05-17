from enum import Enum, EnumMeta


class League(Enum):
    E0 = "Premier League"
    E1 = "Championship"
    D1 = "Bundesliga 1"
    D2 = "Bundesliga 2"

    def __str__(self):
        return self.value

    @classmethod
    def from_string(cls, value):
        for league in cls:
            if league.name == value:
                return league
        raise ValueError(f"No such league: {value}")
