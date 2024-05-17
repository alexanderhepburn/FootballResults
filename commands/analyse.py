from commands.command import Command
from data_manager import data_manager
from command_manager import Colour
import platform
import os


class Analyse(Command):
    def execute(self):
        team_list = []
        print(f"{Colour.BLUE}For a list of teams just type: '*teams'{Colour.END}")
        while True:
            team_input = input(
                f"{Colour.END}Enter team name {Colour.GREEN}{len(team_list) + 1}{Colour.END}: {Colour.PURPLE}")
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
        file_name: str = data_manager().analyse_data(team_list[0], team_list[1])
        print(
            f"{Colour.GREEN}Success! {Colour.BLUE}Report has been generated in the folder exports. Opening file.{Colour.END}")

        os_name = platform.system()

        # Open the file based on the operating system
        if os_name == 'Windows':
            os.startfile(file_name)
        elif os_name == 'Darwin':  # macOS
            os.system('open ' + file_name)
        elif os_name == 'Linux':
            os.system('xdg-open ' + file_name)
        else:
            print(f"Error opening file, please open it manually!")
