import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from settings.user_settings import UserSettings


class Plot:
    def __init__(self, data: pd.DataFrame, team1: str, team2: str, bars_to_create: list[str], team1_wins: int,
                 team1_losses: int, draws: int, correlation_matrix: pd.DataFrame):
        """
        Initializes the Plot object with data and team information.

        Args:
            data (pd.DataFrame): The input data containing match information.
            team1 (str): Name of the first team.
            team2 (str): Name of the second team.
            bars_to_create (list[str]): List of column names to create bar plots for.
            team1_wins (int): Number of wins for the first team.
            team1_losses (int): Number of losses for the first team.
            draws (int): Number of draws between the two teams.
            correlation_matrix (pd.DataFrame): DataFrame containing correlation matrix data.
        """
        self.data = data.rename(index=str.lower, level='Team')
        self.team1 = team1
        self.team2 = team2
        self.bars_to_create = bars_to_create
        self.team1_wins = team1_wins
        self.team1_losses = team1_losses
        self.draws = draws
        self.correlation_matrix = correlation_matrix
        self.date_index = pd.Index(range(UserSettings.get_instance().starting_year,
                                         UserSettings.get_instance().ending_year + 1))

        self.PLOTXY: tuple[int, int] = (10, 6.2)
        self.PADDING = 10

        self.plot_bars()
        self.plot_overall_stats()
        self.plot_correlation_heatmap()

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
        plt.figure(figsize=self.PLOTXY)
        WIDTH = 0.4

        plt.bar(x1 - WIDTH / 2, y1, width=WIDTH, color='skyblue', label=self.team1)
        plt.bar(x2 + WIDTH / 2, y2, width=WIDTH, color='purple', label=self.team2)
        plt.legend(loc="upper left")
        plt.title(title, fontsize=19, fontweight='bold', pad=self.PADDING)
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

            self.create_bar(team1_x, team2_x, team1_y, team2_y, index + 3, column_name)

    def plot_overall_stats(self):
        """
        Plot a pie chart of the overall statistics.
        """
        # Data for the pie plot
        labels = [f'{self.team1} Wins', 'Draws', f'{self.team2} Wins']
        sizes = [self.team1_wins, self.draws, self.team1_losses]
        colors = ['skyblue', 'lightblue', 'purple']

        # Check if sizes list is valid
        if not any(sizes):
            raise ValueError("No data available for plotting overall statistics.")

        fig1, ax1 = plt.subplots(figsize=self.PLOTXY)  # Set figure size here
        wedges, texts, autotexts = ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                                           shadow=False, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Set label colors to white and increase font size
        for text in texts:
            text.set_fontsize(14)

        # Increase font size for autopct texts
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(14)

        plt.title('Overall Statistics', fontsize=19, fontweight='bold', pad=self.PADDING)
        plt.savefig('tmp/plot2.png')

    def plot_correlation_heatmap(self):
        plt.figure(figsize=self.PLOTXY)
        sns.heatmap(self.correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", cbar=False)
        plt.subplots_adjust(bottom=0.2)  # Adjust bottom margin to ensure text is not cut off
        plt.title('Correlation Matrix', fontsize=19, fontweight='bold', pad=self.PADDING)
        plt.savefig('tmp/plot1.png')
