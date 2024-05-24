from misc import setup_program

# For more in-depth information view the README.md file
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
# Structure:
# - commands: main module of the program, where it processes all of the mentioned commands
# - analyse: module that takes care of all the analyse tasks (plotting, pdf creation, data-formatting)
# - settings: module that handels all of the settings functionality
# - misc: module that manages the network, colours and program setup
# - other folders: tmp (temporary for the plots needed for analyse), exports (the exported pdfs), data (all downloaded data)
# Note:
# - This structure allows the program to be modular, with individual commands encapsulated in separate functions or classes.
#   It promotes code organization, maintainability, and ease of adding new features or commands.

if __name__ == '__main__':
    setup_program()  # Download all requirements

    # Imported after SetupProgram to make sure all requirements have been downloaded
    from commands import run_program

    run_program()
