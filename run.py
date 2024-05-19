from misc import setup_program

# TODO update this
# Command Execution Loop:
# - The program enters a loop where it waits for user input.
# - Upon receiving input, it checks if the input matches any available command.
# - If a match is found, the corresponding command is executed.
# - If no match is found, an error message is displayed indicating that the input is invalid.
# Available Commands:
# - Help Command: Provides a list of available commands and their descriptions.
# - Settings Command: Allows the user to view and modify program settings.
# - Teams Command: Displays a list of teams.
# - UpdateData Command: Updates or retrieves data required by the program.
# - Analyse Command: Performs analysis on specified data.
# Note:
# - This structure allows the program to be modular, with individual commands encapsulated in separate functions or classes.
#   It promotes code organization, maintainability, and ease of adding new features or commands.

if __name__ == '__main__':
    setup_program()  # Download all requirements

    # Imported after SetupProgram to make sure all requirements have been downloaded
    from commands import run_program

    run_program()
