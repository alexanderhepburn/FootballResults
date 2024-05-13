import pandas as pd

from data_manager import data_manager
from network_manager import network_manager
from tabulate import tabulate
from settings_manager import settings_manager, InvalidValueError

class command_manager:

    def run_program(self):
        self.__list_of_commands = {"help": {"function" : self.info, "description" : "This function helps you"},
                                   "gamesplayed": {"function" : self.total_games, "description" : "INPUT DESCR"},
                                   "teams": {"function" : self.print_teams, "description" : "Print all available teams."},
                                   "settings": {"function" : self.settings, "description" : "Change the current app settings."},
                                   "analyse": {"function" : self.analyse_teams, "description" : "Analyse two teams."},
                                   "update_data": {"function": self.update_data, "description": "Updates all the data."}}

        print(f"Welcome to the FootballResults program!")
        print(f"For a list of all commands, please type {Colour.GREEN}help{Colour.END}.")

        while True:
            try:
                user_input = input(f"Please enter your command: {Colour.GREEN}")
                print(Colour.END, end="")

                if user_input == "end":
                    print(f"Thank you for using our program! Bye!")
                    return

                if not user_input in self.__list_of_commands:
                    print(f"Error your command: {user_input} is not a valid input!")
                    print(f"Please reenter your command or type {Colour.GREEN}help{Colour.END} for a directory of all commands.")
                    continue

                self.__list_of_commands[user_input]["function"]()
            except KeyError as e:
                print(f"Error Run Program: {e}")

    def info(self):
        print(f"\nPrinting all of the available commands:")
        for method, contents in self.__list_of_commands.items():
            try:
                print(f"{Colour.GREEN}{method}{Colour.END}: {Colour.PURPLE}{contents['description']}{Colour.END}")
            except KeyError:
                print(f"{Colour.GREEN}{method}{Colour.END}: {Colour.RED}No description{Colour.END}")
        print("") # Adding space for readibility

    def total_games(self):
        try:
            df = data_manager.get_all_data()
            while True:
                team_name = input("Please input team name: ").capitalize()
                if (team_name in df['HomeTeam'].values) or (team_name in df['AwayTeam'].values):
                    break
                print("Error team not found, please try again!")

            print("team found")

            total_number_of_games = ((df['HomeTeam'] == team_name) | (df['AwayTeam'] == team_name)).sum()
            print(f"Team: {team_name}, has played a total of {total_number_of_games} times!")
        except Exception as e:
            print(f"Total Games Error: {e}")

    def print_teams(self):
        print(data_manager.get_all_teams())

    def settings(self):
        settings = settings_manager()
        print("Here are your current settings:")

        for index, item in enumerate(settings.settings_data):
            print(f"{item['formatted_name']} ({Colour.PURPLE}{index+1}{Colour.END}):{Colour.GREEN} {item['user']}{Colour.END}")

        while True:
            inputted_setting = input(
                f"Which setting would you like to change (enter the number in purple): {Colour.PURPLE}")
            print(Colour.END, end="") # Changes the colour so that not everything is purple
            try:
                settings_number = int(inputted_setting)
                if settings_number > len(settings.settings_data) or settings_number < 1:
                    print(f"{Colour.RED}{settings_number} is not a valid input, please try again{Colour.END}")
                else:
                    break
            except ValueError as e:
                print(f"{Colour.RED}Invalid Input: Only ints can be entered ({inputted_setting} is not an int){Colour.END}")
            except Exception as e:
                print(f"{Colour.RED}Invalid Input: {e}{Colour.END}")


        while True:
            required_type = settings.settings_data[settings_number - 1]["input_type"]
            inputted_change = input(
                f"What would you like to update ({settings.settings_data[settings_number - 1]['formatted_name']}) to: {Colour.PURPLE}")
            print(Colour.END, end="")  # Changes the colour so that not everything is purple

            try:
                new_value_to_update = required_type(inputted_change)
                new_settings = settings.get_settings()
                new_settings[settings.settings_data[settings_number - 1]["setting"]] = new_value_to_update
                settings_manager().update_settings(new_settings)
                print(f"{Colour.GREEN}Success! {settings.settings_data[settings_number - 1]['formatted_name']} as been updated to: {Colour.PURPLE}{new_value_to_update}{Colour.END}")
                break
            except ValueError as e:
                print(f"{Colour.RED}Invalid Input: Only {required_type} can be entered ({inputted_change} is not of type {required_type}){Colour.END}")
            except InvalidValueError as e:
                print(f"{Colour.RED}Invalid Input ({new_value_to_update}): accepted are {settings.settings_data[settings_number - 1]['accepted_inputs']}{Colour.END}")
            except Exception as e:
                print(f"{Colour.RED}Invalid Input: {e}{Colour.END}")




    def analyse_teams(self):
        team_list = []
        while True:
            team_input = input(f"Enter team name #{len(team_list) + 1}: ")
            if team_input in data_manager.get_all_teams():
                team_list.append(team_input)
            else:
                print("Error please enter a valid team name.")

            if len(team_list) == 2:
                break

        print("Starting analyse")

    def update_data(self):
        print(f"{Colour.GREEN}Updating data!{Colour.END}")
        network_manager.get_all_data()


class Colour:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'