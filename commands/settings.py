from misc import *
from commands.command import Command
from settings import *


class Settings(Command):
    """
    Command to display and update user settings.
    """

    def execute(self):
        """
        Executes the settings command, allowing users to view and update their settings.
        """
        # Display current settings
        print("Here are your current settings:")
        for index, option in enumerate(SettingsManager.settings_data):
            print(
                f"{option} ({PURPLE}{index + 1}{END}):{GREEN} {getattr(UserSettings.get_instance(), option.name)}{END}"
            )

        # Prompt user to select which setting to change
        while True:
            inputted_setting = input(
                f"Which setting would you like to change (enter the number in purple): {PURPLE}"
            ).strip()  # Strip any leading/trailing whitespace
            print(END, end="")  # Reset color formatting
            try:
                settings_number = int(inputted_setting)
                if 1 <= settings_number <= len(SettingsManager.settings_data):
                    break
                else:
                    print(f"{RED}{settings_number} is not a valid input, please try again{END}")
            except ValueError:
                print(
                    f"{RED}Invalid Input: Only ints can be entered ({inputted_setting} is not an int){END}"
                )

        # Prompt user to enter new value for the selected setting
        while True:
            settings_object: SettingsOption = SettingsManager.settings_data[settings_number - 1]
            settings_object.extra_info()  # Display extra info for the setting if available

            inputted_change = input(
                f"What would you like to update ({settings_object}) to: {PURPLE}"
            ).strip()  # Strip any leading/trailing whitespace
            print(END, end="")  # Reset color formatting

            try:
                if settings_object.input_type == League:
                    new_value = League.from_string(inputted_change)
                else:
                    new_value = int(inputted_change)

                settings_object.test(new_value)  # Validate the new value
                UserSettings.update_value(settings_object.name, new_value)  # Update the setting

                print(
                    f"{GREEN}Success! {settings_object} has been updated to: {PURPLE}{inputted_change}{END}"
                )
                break
            except IndexError:
                print(f"{RED}Error: {settings_object.get_error(new_value)}{END}")
            except ValueError:
                print(
                    f"{RED}Invalid Input: Only {settings_object.input_type} can be entered ({inputted_change} is not of type {settings_object.input_type}){END}"
                )
