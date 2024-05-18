from commands.command import Command
from managers.data_manager import DataManager
from managers.command_manager import Colour

from analyse.analyse import Analyse as a
import pandas as pd
from misc.helper_methods import SystemHandling


class Analyse(Command):
    def execute(self):
        team_list = []
        print(f"{Colour.BLUE}For a list of teams just type: '*teams'{Colour.END}")
        while True:
            team_input = input(
                f"{Colour.END}Enter team name {Colour.GREEN}{len(team_list) + 1}{Colour.END}: {Colour.PURPLE}")
            if team_input == "*teams":
                df = pd.DataFrame(DataManager.get_all_teams(), columns=['Teams'])
                print(df)
            elif team_input == "end":
                print(f"{Colour.BLUE}Returning to the main menu.{Colour.END}")
                return
            elif team_input in DataManager.get_all_teams():
                team_list.append(team_input)
            else:
                print(f"{Colour.RED}Error please enter a valid team name.{Colour.END}")

            if len(team_list) == 2:
                print(Colour.END, end="")
                break

        print(f"{Colour.BLUE}Starting analyse...{Colour.END}")

        analyse_data = a(team_list[0], team_list[1]).get_file_name()
        print(
            f"{Colour.GREEN}Success! {Colour.BLUE}Report has been generated in the folder exports. Opening file.{Colour.END}")

        SystemHandling.open_file(analyse_data)
