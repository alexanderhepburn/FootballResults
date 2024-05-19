import requests
from settings.settings_manager import SettingsManager
import os
from tqdm import tqdm
from misc.helper_methods import Colour
from settings.league import League
from settings.settings_manager import SettingsManager


class network_manager:

    @staticmethod
    def get_data(year, league):
        try:
            formatted_year = f"{(year % 100) - 1}{(year % 100)}"
            url = f"https://www.football-data.co.uk/mmz4281/{formatted_year}/{league.name}.csv"
            response = requests.get(url)

            os.makedirs(f"data/{league.name}", exist_ok=True)

            output = open(f"data/{league.name}/{formatted_year}.csv", "wb")
            output.write(response.content)
            output.close()
        except Exception as e:
            print(f"Error Get_data: {e}")

    @staticmethod
    def get_all_data():
        print(f"{Colour.GREEN}Updating data!{Colour.END}")
        accepted_leagues = [league for league in League]
        year_array = list(range(SettingsManager.settings_data[0].min,
                                SettingsManager.settings_data[1].max + 1))
        total_iterations = len(year_array) * len(accepted_leagues)
        with tqdm(total=total_iterations) as pbar:
            for league in accepted_leagues:
                for year in year_array:
                    network_manager.get_data(year, league)
                    pbar.update(1)
        print(f"{Colour.GREEN}Success! Data has been updated!{Colour.END}")

    @staticmethod
    def setup():
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)
        if not os.path.isdir(f'{parent_directory}/data'):
            print(f"{Colour.BLUE}Data upgrade required.")
            network_manager.get_all_data()
