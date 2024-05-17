from settings import Settings
import json


class UserSettings:
    __instance = Settings.user()

    @staticmethod
    def get_instance():
        if UserSettings.__instance == None:
            UserSettings(Settings.user())
        return UserSettings.__instance

    @staticmethod
    def update_value(name, new_value):
        setattr(UserSettings.get_instance(), name, new_value)
        save_file = open("settings.json", "w")
        json.dump(UserSettings.get_instance().to_dict(), save_file)
        save_file.close()

    def __init__(self, settings):
        if UserSettings.__instance != None:
            raise Exception("UserSettings Singleton cannot be instantiated more than once.")
        self.__instance = settings
