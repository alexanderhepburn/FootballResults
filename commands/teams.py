import pandas as pd

from analyse import get_all_teams
from commands.command import Command


class Teams(Command):
    """
    Command to display all teams.
    """

    def execute(self):
        """
        Executes the teams command, displaying a list of all teams.
        """
        # Retrieve and display the list of all teams
        df = pd.DataFrame(get_all_teams(), columns=['Teams'])
        print(df)
