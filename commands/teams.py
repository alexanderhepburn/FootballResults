from commands.command import Command
import pandas as pd
from managers.data_manager import DataManager


class Teams(Command):
    def execute(self):
        df = pd.DataFrame(DataManager.get_all_teams(), columns=['Teams'])
        print(df)
