from .commands import get_commands
from misc import *


def run_program():
    """
    Main function to run the FootballResults program.
    It provides a command-line interface for the user to interact with the program.
    """
    print(f"{BLUE}Welcome to the FootballResults program!{END}")
    print(f"For a list of all commands, please type {GREEN}help{END}.")

    while True:
        try:
            found_match = False
            user_input = input(
                f"Please enter your command: {GREEN}").strip()  # Get user input and remove leading/trailing whitespace
            print(END, end="")  # Reset color formatting

            if user_input.lower() == "end":  # End the program if the user types 'end'
                print(f"{BLUE}Thank you for using our program! Bye!{END}")
                return

            if user_input.lower() == "help":  # Show help if the user types 'help'
                found_match = True
                print(f"{BLUE}Printing all of the available commands:{END}")
                for command in get_commands():
                    print(f"{GREEN}{command.command_name}{END}: {PURPLE}{command.command_description}{END}")

            for command in get_commands():  # Iterate through all commands
                if command.command_name == user_input:
                    command.execute()  # Execute the command if it matches user input
                    found_match = True

            if not found_match:  # If no valid command was found, print an error message
                print(f"Error: your command '{user_input}' is not a valid input!")
                print(f"Please reenter your command or type {GREEN}help{END} for a directory of all commands.")
        except KeyError as e:
            print(f"Error Run Program: {e}")  # Handle KeyError exceptions
