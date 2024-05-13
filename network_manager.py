import pandas as pd
import requests
from settings_manager import settings_manager
import os

class network_manager:

    @staticmethod
    def get_data(year, league):
        try:
            formatted_year = f"{(year % 100)-1}{(year % 100)}"
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
        settings = settings_manager()
        year_array = [x for x in range(settings.min_start_year, settings.max_end_year)]
        for league in settings.accepted_leagues:
            for year in year_array:
                network_manager.get_data(year, league)