import matplotlib.pyplot as plt
import pandas as pd
from settings.user_settings import UserSettings


class Plot:
    def create_bar(self, x1: list, x2: list, y1: pd.Index, y2: pd.Index, yAll: pd.Index, x1_name: str, x2_name: str,
                   plot_number: int,
                   title: str):
        plt.figure(figsize=(10, 6))
        # Width of a bar
        WIDTH = 0.4

        plt.bar(y1 - (WIDTH / 2), x1, width=WIDTH, color='skyblue',
                label=x1_name)
        plt.bar(y2 + (WIDTH / 2), x2, width=WIDTH, color='purple',
                label=x2_name)
        plt.legend(loc="upper left")
        plt.title(title)
        plt.xticks(yAll)
        plt.grid(axis='y', alpha=0.7)

        plt.savefig(f'tmp/plot{plot_number}.png')
        plt.close()  # For memory reasons, figures need to be closed

    def __init__(self, data: pd.DataFrame, team1: str, team2: str, bars_to_create: list[str]):
        date = pd.Index(
            list(range(UserSettings.get_instance().starting_year, UserSettings.get_instance().ending_year + 1)))

        for index, column_name in enumerate(bars_to_create):
            self.create_bar(data.rename(index=str.lower, level='Team').xs(team1.lower(), level="Team")[column_name],
                            data.rename(index=str.lower, level='Team').xs(team2.lower(), level="Team")[column_name],
                            data.rename(index=str.lower, level='Team').xs(team1.lower(),
                                                                          level="Team").index.get_level_values(
                                'Date'),
                            data.rename(index=str.lower, level='Team').xs(team2.lower(),
                                                                          level="Team").index.get_level_values(
                                'Date'), date, team1,
                            team2, index + 1,
                            column_name)
