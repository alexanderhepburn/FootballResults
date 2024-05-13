import pandas as pd
from helper_methods import Colour
from data_manager import data_manager
from network_manager import network_manager
from tabulate import tabulate
from settings_manager import settings_manager, InvalidValueError
import os

class command_manager:

    def run_program(self):
        self.__list_of_commands = {"help": {"function" : self.info, "description" : "This function helps you"},
                                   "end": {"function": None, "description": "Ends the program."},
                                   "teams": {"function" : self.print_teams, "description" : "Print all available teams."},
                                   "settings": {"function" : self.settings, "description" : "Change the current app settings."},
                                   "analyse": {"function" : self.analyse_teams, "description" : "Analyse two teams."},
                                   "update_data": {"function": self.update_data, "description": "Updates all the data."}}

        print(f"{Colour.BLUE}Welcome to the FootballResults program!{Colour.END}")
        network_manager.setup()
        print(f"For a list of all commands, please type {Colour.GREEN}help{Colour.END}.")

        while True:
            try:
                user_input = input(f"Please enter your command: {Colour.GREEN}")
                print(Colour.END, end="")

                if user_input == "end":
                    print(f"{Colour.BLUE}Thank you for using our program! Bye!{Colour.END}")
                    return

                if not user_input in self.__list_of_commands:
                    print(f"Error your command: {user_input} is not a valid input!")
                    print(f"Please reenter your command or type {Colour.GREEN}help{Colour.END} for a directory of all commands.")
                    continue

                self.__list_of_commands[user_input]["function"]()
            except KeyError as e:
                print(f"Error Run Program: {e}")

    def info(self):
        print(f"{Colour.BLUE}Printing all of the available commands:{Colour.END}")
        for method, contents in self.__list_of_commands.items():
            try:
                print(f"{Colour.GREEN}{method}{Colour.END}: {Colour.PURPLE}{contents['description']}{Colour.END}")
            except KeyError:
                print(f"{Colour.GREEN}{method}{Colour.END}: {Colour.RED}No description{Colour.END}")

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
        df = pd.DataFrame(data_manager.get_all_teams(), columns=['Teams'])
        print(df)

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
        print(f"{Colour.BLUE}For a list of teams just type: '*teams'{Colour.END}")
        while True:
            team_input = input(f"{Colour.END}Enter team name {Colour.GREEN}{len(team_list) + 1}{Colour.END}: {Colour.PURPLE}")
            if team_input == "*teams":
                self.print_teams()
            elif team_input == "end":
                print(f"{Colour.BLUE}Returning to the main menu.{Colour.END}")
                return
            elif team_input in data_manager.get_all_teams():
                team_list.append(team_input)
            else:
                print(f"{Colour.RED}Error please enter a valid team name.{Colour.END}")

            if len(team_list) == 2:
                print(Colour.END, end="")
                break

        print(f"{Colour.BLUE}Starting analyse...{Colour.END}")
        file_name = data_manager.analyse_data(team_list[0], team_list[1])
        print(f"{Colour.GREEN}Success! {Colour.BLUE}Report has been generated in the folder exports. Opening file.{Colour.END}")
        try:
            os.system(f"open {file_name}")
        except Exception as e:
            print(f"Error opening file: {e}")


    def update_data(self):
        network_manager.get_all_data()