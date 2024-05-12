import pandas as pd

from data_manager import data_manager
from network_manager import network_manager
from tabulate import tabulate

class command_manager:

    def run_program(self):
        self.__list_of_commands = {"help": {"function" : self.info, "description" : "This function helps you"},
                                   "gamesplayed": {"function" : self.total_games, "description" : "INPUT DESCR"},
                                   "teams": {"function" : self.print_teams, "description" : "Print all available teams."},
                                   "settings": {"function" : self.settings, "description" : "Change the current app settings."},
                                   "analyse": {"function" : self.analyse_teams, "description" : "Analyse two teams."}}

        print(f"Welcome to the FootballResults program!")
        print(f"For a list of all commands, please type help.")

        while True:
            try:
                user_input = input(f"Please enter your command: ")

                if user_input == "end":
                    print(f"Thank you for using our program! Bye!")
                    return

                if not user_input in self.__list_of_commands:
                    print(f"Error your command: {user_input} is not a valid input!")
                    print(f"Please reenter your command or type help for a directory of all commands.")
                    continue

                self.__list_of_commands[user_input]["function"]()
            except KeyError as e:
                print(f"Error Run Program: {e}")

    def info(self):
        print(f"\nPrinting all of the available commands:")
        for method, contents in self.__list_of_commands.items():
            try:
                print(f"{method}: {contents['description']}")
            except KeyError:
                print(f"{method}: No description")
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
        print("WPI")
        # Einige Einstellungen beispielsweise Jahre und League?

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
