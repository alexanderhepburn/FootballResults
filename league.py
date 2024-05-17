from enum import Enum


class League(Enum):
    E0 = "Premier League"
    E1 = "Championship"
    D1 = "Bundesliga 1"
    D2 = "Bundesliga 2"

    def __str__(self):
        return self.value
