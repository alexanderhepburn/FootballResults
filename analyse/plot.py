import matplotlib.pyplot as plt
import pandas as pd
from settings.user_settings import UserSettings


class Plot:
    def __init__(self, data: pd.DataFrame, team1: str, team2: str, bars_to_create: list[str]):
        """
        Initializes the Plot object with data and team information.

        Args:
            data (pd.DataFrame): The input data containing team information.
            team1 (str): Name of the first team.
            team2 (str): Name of the second team.
            bars_to_create (list[str]): List of column names to create bar plots for.
        """
        self.data = data.rename(index=str.lower, level='Team')
        self.team1 = team1
        self.team2 = team2
        self.bars_to_create = bars_to_create
        self.date_index = pd.Index(range(UserSettings.get_instance().starting_year,
                                         UserSettings.get_instance().ending_year + 1))
        self.plot_bars()

    def create_bar(self, x1: pd.Index, x2: pd.Index, y1: pd.Series, y2: pd.Series, plot_number: int, title: str):
        """
        Creates a bar plot comparing two teams over time.

        Args:
            x1 (pd.Series): Data for the first team.
            x2 (pd.Series): Data for the second team.
            y1 (pd.Index): Date index for the first team.
            y2 (pd.Index): Date index for the second team.
            plot_number (int): Plot number for saving the file.
            title (str): Title of the plot.
        """
        plt.figure(figsize=(10, 6))
        WIDTH = 0.4

        plt.bar(x1 - WIDTH / 2, y1, width=WIDTH, color='skyblue', label=self.team1)
        plt.bar(x2 + WIDTH / 2, y2, width=WIDTH, color='purple', label=self.team2)
        plt.legend(loc="upper left")
        plt.title(title)
        plt.xticks(self.date_index)
        plt.grid(axis='y', alpha=0.7)

        plt.savefig(f'tmp/plot{plot_number}.png')
        plt.close()

    def plot_bars(self):
        """
        Iterates through the list of columns and creates bar plots for each.
        """
        for index, column_name in enumerate(self.bars_to_create):
            team1_y = self.data.xs(self.team1.lower(), level='Team')[column_name]
            team2_y = self.data.xs(self.team2.lower(), level='Team')[column_name]
            team1_x = team1_y.index.get_level_values('Date')
            team2_x = team2_y.index.get_level_values('Date')

            self.create_bar(team1_x, team2_x, team1_y, team2_y, index + 1, column_name)
