from league import League
import json


class Settings:

    def __init__(self, starting_year: int, ending_year: int, league: League):
        self.starting_year = starting_year
        self.ending_year = ending_year
        self.league = league

    @classmethod
    def default(cls):
        return cls(2010, 2024, League.E0)

    @classmethod
    def user(cls):
        with open('settings.json', 'r') as file:
            json_data = json.load(file)
            return cls(json_data["starting_year"], json_data["ending_year"], League[json_data["league"]])

    def update_attribute(self, attribute_name, value):
        if hasattr(self, attribute_name):
            setattr(self, attribute_name, value)
        else:
            raise AttributeError(f"'Settings' object has no attribute '{attribute_name}'")

    def to_dict(self) -> dict[str: any]:
        return {"league": self.league.name, "starting_year": self.starting_year, "ending_year": self.ending_year}
