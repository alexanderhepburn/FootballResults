import json
from settings.league import League
from settings.settings import Settings
from settings.user_settings import UserSettings
from settings.settings_option import RangeSettingsOption, ListSettingsOption, SettingsOption


class SettingsManager:
    user_settings: Settings = UserSettings.get_instance()

    settings_data: SettingsOption = [
        RangeSettingsOption("starting_year", "Starting Year", 2010, user_settings.ending_year),
        RangeSettingsOption("ending_year", "Ending Year", user_settings.starting_year, 2024),
        ListSettingsOption("league", "League", [league for league in League])]

    @staticmethod
    def reset_settings():
        SettingsManager.update_settings(Settings.default().to_dict())
        UserSettings.update_settings(Settings.default())

    @classmethod
    def refresh_settings(cls):
        user: Settings = UserSettings.get_instance()
        cls.user_settings = user
        cls.settings_data[0]["user"] = user.starting_year
        cls.settings_data[1]["user"] = user.ending_year
        cls.settings_data[2]["user"] = user.league
