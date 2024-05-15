import pandas as pd
import json
import settings_manager

class settings_manager:

    max_end_year = 2024
    min_start_year = 2010
    accepted_leagues = ["E0", "E1", "D1", "D2"]

    def __init__(self):
        self.user_start_year = self.get_settings()["starting_year"]
        self.user_end_year = self.get_settings()["ending_year"]
        self.user_league = self.get_settings()["league"]

        self.settings_data = [{"setting": "starting_year", "formatted_name": "Starting Year", "user": self.user_start_year, "input_type": int, "accepted_inputs": f"values less than: {self.user_end_year} and greater than: {self.min_start_year - 1}"},
                         {"setting": "ending_year", "formatted_name": "Ending Year", "user": self.user_end_year, "input_type": int, "accepted_inputs": f"values greater than: {self.user_start_year} and less than: {self.max_end_year + 1}"},
                         {"setting": "league", "formatted_name": "League", "user": self.user_league, "input_type": str, "accepted_inputs": f"the following values: {self.accepted_leagues}"}]

    def get_settings(self):
        with open('settings.json', 'r') as file:
            json_data = json.load(file)
            return json_data

    def update_settings(self, dictionary_input):
        if (dictionary_input["starting_year"] < self.min_start_year
                or dictionary_input["starting_year"] >= self.user_end_year
                or dictionary_input["ending_year"] > self.max_end_year
                or dictionary_input["ending_year"] <= self.user_start_year
                or not dictionary_input["league"] in self.accepted_leagues):
            raise InvalidValueError
        save_file = open("settings.json", "w")
        json.dump(dictionary_input, save_file)
        save_file.close()

    def reset_settings(self):
        settings_manager.update_settings({"league": "E0", "starting_year": self.min_start_year, "ending_year": self.max_end_year})

class InvalidValueError(Exception):
    pass