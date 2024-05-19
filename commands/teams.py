import pandas as pd

from analyse import get_all_teams
from commands.command import Command


class Teams(Command):
    def execute(self):
        df = pd.DataFrame(get_all_teams(), columns=['Teams'])
        print(df)
