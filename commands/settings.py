import misc.colour as c
from commands.command import Command
from settings import *


class Settings(Command):
    def execute(self):
        print("Here are your current settings:")
        for index, option in enumerate(SettingsManager.settings_data):
            print(
                f"{option} ({c.PURPLE}{index + 1}{c.END}):{c.GREEN} {getattr(UserSettings.get_instance(), option.name)}{c.END}")

        while True:
            inputted_setting = input(
                f"Which setting would you like to change (enter the number in purple): {c.PURPLE}")
            print(c.END, end="")  # Changes the colour so that not everything is purple
            try:
                settings_number = int(inputted_setting)
                if settings_number > len(SettingsManager.settings_data) or settings_number < 1:
                    print(f"{c.RED}{settings_number} is not a valid input, please try again{c.END}")
                else:
                    break
            except ValueError as e:
                print(
                    f"{c.RED}Invalid Input: Only ints can be entered ({inputted_setting} is not an int){c.END}")

        while True:
            settings_object: SettingsOption = SettingsManager.settings_data[settings_number - 1]
            settings_object.extra_info()

            inputted_change = input(
                f"What would you like to update ({settings_object}) to: {c.PURPLE}")
            print(c.END, end="")  # Changes the colour so that not everything is purple

            try:
                if settings_object.input_type == League:
                    new_value = League.from_string(inputted_change)
                else:
                    new_value = int(inputted_change)

                settings_object.test(new_value)
                UserSettings.update_value(settings_object.name, new_value)

                print(
                    f"{c.GREEN}Success! {settings_object} as been updated to: {c.PURPLE}{inputted_change}{c.END}")
                break
            except IndexError as e:
                print(f"{c.RED}Error: {settings_object.get_error(new_value)}{c.END}")
            except ValueError as e:
                print(
                    f"{c.RED}Invalid Input: Only {settings_object.input_type} can be entered ({inputted_change} is not of type {settings_object.input_type}){c.END}")
