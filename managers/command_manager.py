from commands.commands import Commands
from managers.network_manager import NetworkManager
from misc.helper_methods import Colour


class CommandManager:
    @staticmethod
    def run_program():
        print(f"{Colour.BLUE}Welcome to the FootballResults program!{Colour.END}")
        NetworkManager.setup()
        print(f"For a list of all commands, please type {Colour.GREEN}help{Colour.END}.")

        while True:
            try:
                found_match = False
                user_input = input(f"Please enter your command: {Colour.GREEN}")
                print(Colour.END, end="")

                if user_input == "end":
                    print(f"{Colour.BLUE}Thank you for using our program! Bye!{Colour.END}")
                    return

                if user_input == "help":
                    found_match = True
                    print(f"{Colour.BLUE}Printing all of the available commands:{Colour.END}")
                    for command in Commands.commands:
                        print(
                            f"{Colour.GREEN}{command.command_name}{Colour.END}: {Colour.PURPLE}{command.command_description}{Colour.END}")

                for command in Commands.commands:
                    if command.command_name == user_input:
                        command.execute()
                        found_match = True

                if not found_match:
                    print(f"Error your command: {user_input} is not a valid input!")
                    print(
                        f"Please reenter your command or type {Colour.GREEN}help{Colour.END} for a directory of all commands.")
            except KeyError as e:
                print(f"Error Run Program: {e}")
