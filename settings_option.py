from user_settings import UserSettings
from command_manager import Colour
from league import League


class SettingsOption:

    def __init__(self, name: str, formatted_name: str):
        self.name = name
        self.__formatted_name = formatted_name
        self.setting = getattr(UserSettings.get_instance(), name)
        self.input_type = type(self.setting)

    def __str__(self):
        return self.__formatted_name

    def test(self, value) -> bool:
        raise NotImplementedError

    def get_error(self, value) -> str:
        raise NotImplementedError

    def extra_info(self) -> None:
        return None


class RangeSettingsOption(SettingsOption):

    def __init__(self, name: str, formatted_name: str, min: int, max: int):
        super().__init__(name, formatted_name)
        self.min = min
        self.max = max

    def test(self, value: int):
        if not (self.min <= value <= self.max):
            raise IndexError

    def get_error(self, value: int) -> str:
        return f"The input ({value}) must be inbetween {self.min} and {self.max}!"


class ListSettingsOption(SettingsOption):

    def __init__(self, name: str, formatted_name: str, list_of_strings: list[str]):
        super().__init__(name, formatted_name)
        self.list_of_strings = list_of_strings

    def test(self, value: str):
        if value not in self.list_of_strings:
            raise IndexError

    def get_error(self, value) -> str:
        return f"The input ({value}) is not in: {value}!"

    def extra_info(self) -> None:
        print(f"Following Team Options (please enter the {Colour.PURPLE}two digit combination{Colour.END}):")
        for league in League:
            print(f"{Colour.BLUE}{league.value}{Colour.END}: {Colour.PURPLE}{league.name}{Colour.END}")
