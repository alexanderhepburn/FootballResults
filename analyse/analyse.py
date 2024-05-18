from analyse.pdf_creator import PdfCreator as creator
from analyse.plot import Plot as p
from managers.data_manager import DataManager  #
import pandas as pd

from settings.user_settings import UserSettings


class Analyse:

    def __init__(self, team1: str, team2: str):
        self.team1 = team1
        self.team2 = team2
        self._analyse_data()

    def get_file_name(self) -> str:
        try:
            return self._file_name
        except NameError:
            raise FileExistsError("Error with the creation of the file.")

    def _analyse_data(self):

        team_data = DataManager.get_data_with_columns([self.team1, self.team2])

        ## TODO BESSER MACHEN

        date = pd.Index(
            list(range(UserSettings.get_instance().starting_year, UserSettings.get_instance().ending_year + 1)))

        for i in range(1, 9):
            p().create_bar(team_data.xs(self.team1, level="Team")["Full Time Team Goals"],
                           team_data.xs(self.team2, level="Team")["Full Time Team Goals"],
                           team_data.xs(self.team1, level="Team").index.get_level_values('Date'),
                           team_data.xs(self.team2, level="Team").index.get_level_values('Date'), date, self.team1,
                           self.team2, i,
                           "Full Time Team Goals")

        pdf_name = creator().create(self.team1, self.team2)
        self._file_name = pdf_name

        ## Shots on Target
        ## Corner, Fouls, Free kicks
        ## Rote und Gelbe Karte
