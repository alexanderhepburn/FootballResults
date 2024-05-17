import pandas as pd
import requests
from settings_manager import SettingsManager
import os
from tqdm import tqdm
from helper_methods import Colour


class network_manager:

    @staticmethod
    def get_data(year, league):
        try:
            formatted_year = f"{(year % 100) - 1}{(year % 100)}"
            url = f"https://www.football-data.co.uk/mmz4281/{formatted_year}/{league}.csv"
            response = requests.get(url)

            os.makedirs(f"data/{league}", exist_ok=True)

            output = open(f"data/{league}/{formatted_year}.csv", "wb")
            output.write(response.content)
            output.close()
        except Exception as e:
            print(f"Error Get_data: {e}")

    @staticmethod
    def get_all_data():
        print(f"{Colour.GREEN}Updating data!{Colour.END}")
        settings = SettingsManager()
        year_array = [x for x in range(settings.min_start_year, settings.max_end_year + 1)]
        total_iterations = len(year_array) * len(settings.accepted_leagues)
        with tqdm(total=total_iterations) as pbar:
            for league in settings.accepted_leagues:
                for year in year_array:
                    network_manager.get_data(year, league)
                    pbar.update(1)
        print(f"{Colour.GREEN}Success! Data has been updated!{Colour.END}")

    @staticmethod
    def setup():
        DIR = 'data/E0'
        if not os.path.isdir('data'):
            print(f"{Colour.BLUE}Data upgrade required.")
            network_manager.get_all_data()
