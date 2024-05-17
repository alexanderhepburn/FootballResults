import json
from league import League
from settings import Settings


class SettingsManager:
    max_ending_year: int = 2024
    min_starting_year: int = 2010
    accepted_leagues: list[str] = [league.name for league in League]

    user_settings: Settings = Settings.user()

    settings_data = [
        {"setting": "starting_year", "formatted_name": "Starting Year", "user": user_settings.starting_year,
         "input_type": int,
         "accepted_inputs": f"values less than: {user_settings.ending_year} and greater than: {min_starting_year - 1}"},
        {"setting": "ending_year", "formatted_name": "Ending Year", "user": user_settings.ending_year,
         "input_type": int,
         "accepted_inputs": f"values greater than: {user_settings.starting_year} and less than: {max_ending_year + 1}"},
        {"setting": "league", "formatted_name": "League", "user": user_settings.league, "input_type": str,
         "accepted_inputs": f"the following values: {accepted_leagues}"}]

    @staticmethod
    def update_settings(new_settings: Settings):
        if (new_settings.starting_year < SettingsManager.min_starting_year
                or new_settings.starting_year >= SettingsManager.user_settings.ending_year
                or new_settings.ending_year > SettingsManager.max_ending_year
                or new_settings.ending_year <= SettingsManager.user_settings.starting_year
                or not new_settings.league.name in SettingsManager.accepted_leagues):
            raise InvalidValueError
        save_file = open("settings.json", "w")
        json.dump(new_settings.to_dict(), save_file)
        save_file.close()
        SettingsManager.user_settings = new_settings

    @staticmethod
    def reset_settings():
        SettingsManager.update_settings(Settings.default().to_dict())

    @classmethod
    def refresh_settings(cls):
        user: Settings = Settings.user()
        cls.user_settings = user
        cls.settings_data[0]["user"] = user.starting_year
        cls.settings_data[1]["user"] = user.ending_year
        cls.settings_data[2]["user"] = user.league


class InvalidValueError(Exception):
    pass
