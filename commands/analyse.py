from analyse import *
from misc import *
from .command import Command


class Analyse(Command):
    """
    Represents a command for analyzing football data.

    This command allows users to select two teams for analysis, generate a report, and open the report file.
    """

    def execute(self):
        team_list = []
        print(f"{BLUE}For a list of teams just type: '*teams'{END}")
        while True:
            teams = get_all_teams()
            team_input = input(
                f"{END}Enter team name {GREEN}{len(team_list) + 1}{END}: {PURPLE}").lower()
            if team_input == "*teams":  # If user requests team list
                df = pd.DataFrame(teams, columns=['Teams'])
                print(df)
            elif team_input == "end":  # If user wants to end selection process
                print(f"{BLUE}Returning to the main menu.{END}")
                return
            elif team_input in [s.lower() for s in teams]:  # If user input matches a team name
                formatted_team = next(team for team in teams if team.lower() == team_input)  # Get formatted team name
                team_list.append(formatted_team)
            else:  # If user input does not match any team name print error
                print(f"{RED}Error please enter a valid team name.{END}")

            if len(team_list) == 2:  # If two teams have been selected reset color formatting and exit loop
                print(END, end="")
                break

        print(f"{BLUE}Starting analyse...{END}")

        # Generate report file and get file name
        analyse_data = analyse(team_list[0], team_list[1])

        # Print success message with file location
        print(
            f"{GREEN}Success! {BLUE}Report has been generated in the folder exports. Opening file.{END}")
        print(
            f"{BLUE}The file name is located at: {analyse_data}{END}")

        open_file(analyse_data)  # Open the report file
