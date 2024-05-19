from settings.user_settings import UserSettings
from managers.command_manager import Colour
from settings.league import League


class SettingsOption:
    """
    Represents a generic setting option.

    Attributes:
        name (str): The name of the setting.
        setting (any): The current value of the setting.
        input_type (type): The data type of the setting value.
    """

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
    """
    Represents a setting option with a range of valid values.

    Attributes:
        min (int): The minimum value of the range.
        max (int): The maximum value of the range.
    """

    def __init__(self, name: str, formatted_name: str, min: int, max: int):
        super().__init__(name, formatted_name)
        self.min = min
        self.max = max

    def test(self, value: int):
        """
        Test if the provided value is within the valid range.

        Args:
            value (int): The value to be tested.

        Raises:
            IndexError: If the value is not within the valid range.
        """
        if not (self.min <= value <= self.max):
            raise IndexError

    def get_error(self, value: int) -> str:
        """
       Returns an error message for an invalid value within the range.

       Args:
           value (int): The invalid value.

       Returns:
           str: The error message.
       """
        return f"The input ({value}) must be inbetween {self.min} and {self.max}!"


class ListSettingsOption(SettingsOption):
    """
    Represents a setting option with a list of valid values.

    Attributes:
        list_of_strings (list[str]): The list of valid values.
    """

    def __init__(self, name: str, formatted_name: str, list_of_strings: list[str]):
        super().__init__(name, formatted_name)
        self.list_of_strings = list_of_strings

    def test(self, value: str):
        """
        Test if the provided value is in the list of valid values.

        Args:
            value (str): The value to be tested.

        Raises:
            IndexError: If the value is not in the list of valid values.
        """
        if value not in self.list_of_strings:
            raise IndexError

    def get_error(self, value) -> str:
        """
        Returns an error message for an invalid value not in the list.

        Args:
            value (str): The invalid value.

        Returns:
            str: The error message.
        """
        return f"The input ({value}) is not in: {value}!"

    def extra_info(self) -> None:
        """
        Provides extra information about the setting (list of valid values).

        Returns:
            None
        """
        print(f"Following Team Options (please enter the {Colour.PURPLE}two digit combination{Colour.END}):")
        for league in League:
            print(f"{Colour.BLUE}{league.value}{Colour.END}: {Colour.PURPLE}{league.name}{Colour.END}")
