from .commands import get_commands
from misc import *


def run_program():
    print(f"{BLUE}Welcome to the FootballResults program!{END}")
    print(f"For a list of all commands, please type {GREEN}help{END}.")

    while True:
        try:
            found_match = False
            user_input = input(f"Please enter your command: {GREEN}")
            print(END, end="")

            if user_input == "end":
                print(f"{BLUE}Thank you for using our program! Bye!{END}")
                return

            if user_input == "help":
                found_match = True
                print(f"{BLUE}Printing all of the available commands:{END}")
                for command in get_commands():
                    print(
                        f"{GREEN}{command.command_name}{END}: {PURPLE}{command.command_description}{END}")

            for command in get_commands():
                if command.command_name == user_input:
                    command.execute()
                    found_match = True

            if not found_match:
                print(f"Error your command: {user_input} is not a valid input!")
                print(
                    f"Please reenter your command or type {GREEN}help{END} for a directory of all commands.")
        except KeyError as e:
            print(f"Error Run Program: {e}")
