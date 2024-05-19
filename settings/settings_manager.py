import json
from settings.league import League
from settings.settings import Settings
from settings.user_settings import UserSettings
from settings.settings_option import RangeSettingsOption, ListSettingsOption, SettingsOption


class SettingsManager:
    """
    A class responsible for managing user settings and providing methods to update, reset, and refresh settings.

    Attributes:
        user_settings (Settings): An instance of user settings retrieved from UserSettings.
        settings_data (SettingsOption): A list containing settings options such as starting year, ending year, and league.
    """

    # Get the instance of user settings
    user_settings: Settings = UserSettings.get_instance()

    # Define settings data with default values
    settings_data: SettingsOption = [
        RangeSettingsOption("starting_year", "Starting Year", 2010, user_settings.ending_year),
        RangeSettingsOption("ending_year", "Ending Year", user_settings.starting_year, 2024),
        ListSettingsOption("league", "League", [league for league in League])]

    @staticmethod
    def reset_settings():
        """
        Resets the settings to their default values.
        """
        SettingsManager.update_settings(Settings.default().to_dict())
        UserSettings.update_settings(Settings.default())

    @classmethod
    def refresh_settings(cls):
        """
        Refreshes the settings data based on the current user settings.

        This method updates the settings data with the current values from the user settings.
        """
        user: Settings = UserSettings.get_instance()
        cls.user_settings = user
        cls.settings_data[0]["user"] = user.starting_year
        cls.settings_data[1]["user"] = user.ending_year
        cls.settings_data[2]["user"] = user.league
