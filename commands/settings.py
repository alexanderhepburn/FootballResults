from commands.command import Command
from command_manager import Colour
from settings_manager import SettingsManager
from settings_option import SettingsOption
from user_settings import UserSettings
from league import League


class Settings(Command):
    def execute(self):
        print("Here are your current settings:")
        for index, option in enumerate(SettingsManager.settings_data):
            print(
                f"{option} ({Colour.PURPLE}{index + 1}{Colour.END}):{Colour.GREEN} {getattr(UserSettings.get_instance(), option.name)}{Colour.END}")

        while True:
            inputted_setting = input(
                f"Which setting would you like to change (enter the number in purple): {Colour.PURPLE}")
            print(Colour.END, end="")  # Changes the colour so that not everything is purple
            try:
                settings_number = int(inputted_setting)
                if settings_number > len(SettingsManager.settings_data) or settings_number < 1:
                    print(f"{Colour.RED}{settings_number} is not a valid input, please try again{Colour.END}")
                else:
                    break
            except ValueError as e:
                print(
                    f"{Colour.RED}Invalid Input: Only ints can be entered ({inputted_setting} is not an int){Colour.END}")

        while True:
            settings_object: SettingsOption = SettingsManager.settings_data[settings_number - 1]
            settings_object.extra_info()

            inputted_change = input(
                f"What would you like to update ({settings_object}) to: {Colour.PURPLE}")
            print(Colour.END, end="")  # Changes the colour so that not everything is purple

            try:
                if settings_object.input_type == League:
                    new_value = League.from_string(inputted_change)
                else:
                    new_value = int(inputted_change)

                settings_object.test(new_value)
                UserSettings.update_value(settings_object.name, new_value)

                print(
                    f"{Colour.GREEN}Success! {settings_object} as been updated to: {Colour.PURPLE}{inputted_change}{Colour.END}")
                break
            except IndexError as e:
                print(f"{Colour.RED}Error: {settings_object.get_error(new_value)}{Colour.END}")
            except ValueError as e:
                print(
                    f"{Colour.RED}Invalid Input: Only {settings_object.input_type} can be entered ({inputted_change} is not of type {settings_object.input_type}){Colour.END}")
