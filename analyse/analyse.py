from analyse.pdf_creator import PdfCreator as creator
from analyse.plot import Plot as p
from managers.data_manager import DataManager  #


class Analyse:

    def __init__(self, team1: str, team2: str):
        team_data = DataManager.get_data_with_columns([team1, team2])

        p(team_data, team1, team2,
          ['Full Time Goals', 'Half Time Goals', 'Shots on Target', 'Shots',
           'Fouls Committed',
           'Corners', 'Yellow Cards', 'Red Cards'])

        pdf_name = creator().create(team1, team2)
        self._file_name = pdf_name

    def get_file_name(self) -> str:
        try:
            return self._file_name
        except NameError:
            raise FileExistsError("Error with the creation of the file.")
