import pandas as pd

from data_manager import data_manager
from network_manager import network_manager
from tabulate import tabulate

class command_manager:

    def run_program(self):
        self.__list_of_commands = {"help": {"function" : self.info, "description" : "This function helps you"},
                                   "gamesplayed": {"function" : self.total_games, "description" : "INPUT DESCR"},
                                   "teams": {"function" : self.print_teams, "description" : "INPUT DESCR"}}

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
            except KeyError:
                print("Error Function")

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
        except:
            print("ERRORORROROROROR")

    def print_teams(self):
        try:
            df = data_manager.get_all_data()
            unique_values_list = list(set(df['HomeTeam'].unique()).union(df['AwayTeam'].unique()))

            print(unique_values_list)
        except:
            print("ERRORORROROROROR")