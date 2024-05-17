from commands.command import Command
import pandas as pd
from managers.data_manager import data_manager


class Teams(Command):
    def execute(self):
        df = pd.DataFrame(data_manager.get_all_teams(), columns=['Teams'])
        print(df)
