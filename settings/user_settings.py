import json

from settings.settings import Settings


class UserSettings:
    """
    Represents user settings, implemented as a Singleton pattern.

    This class provides methods to retrieve the current settings instance, update settings values,
    and initialize the singleton instance.
    """

    __instance = Settings.user()

    def __init__(self, settings):
        """
        Initializes the UserSettings singleton instance.

        Args:
            settings (Settings): The initial settings instance.
        """
        if UserSettings.__instance != None:
            raise Exception("UserSettings Singleton cannot be instantiated more than once.")
        self.__instance = settings

    @staticmethod
    def get_instance():
        """
        Retrieves the current singleton instance of UserSettings.

        Returns:
            UserSettings: The current singleton instance of UserSettings.
        """
        if UserSettings.__instance == None:
            UserSettings(Settings.user())
        return UserSettings.__instance

    @staticmethod
    def update_value(name, new_value):
        """
        Updates the value of a setting attribute and saves the updated settings to a JSON file.

        Args:
            name (str): The name of the setting attribute to be updated.
            new_value (any): The new value for the setting attribute.
        """
        setattr(UserSettings.get_instance(), name, new_value)
        save_file = open("settings/settings.json", "w")
        json.dump(UserSettings.get_instance().to_dict(), save_file)
        save_file.close()
