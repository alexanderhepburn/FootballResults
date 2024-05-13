import pandas as pd
import json
import settings_manager

class settings_manager:

    max_start_year = [2023]
    min_end_year = [2010]
    accepted_leagues = ["E0", "E1", "D1", "D2"]

    def __init__(self):
        self.user_start_year = self.get_settings()["starting_year"]
        self.user_end_year = self.get_settings()["ending_year"]
        self.user_league = self.get_settings()["league"]

        self.settings_data = [{"setting": "starting_year", "formatted_name": "Starting Year", "user": self.user_start_year, "input_type": int},
                         {"setting": "ending_year", "formatted_name": "Ending Year", "user": self.user_end_year, "input_type": int},
                         {"setting": "league", "formatted_name": "League", "user": self.user_league, "input_type": str}]

    def get_settings(self):
        with open('settings.json', 'r') as file:
            json_data = json.load(file)
            return json_data

    def update_settings(self, dictionary_input):
        try:
            if (dictionary_input["starting_year"] > self.max_start_year
                    or dictionary_input["ending_year"] < self.min_end_year
                    or not dictionary_input["league"] in self.accepted_leagues):
                raise Exception
            save_file = open("settings.json", "w")
            json.dump(dictionary_input, save_file)
            save_file.close()
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def reset_settings():
        settings_manager.update_settings({"league": "E0", "starting_year": 2010, "ending_year": 2023})
