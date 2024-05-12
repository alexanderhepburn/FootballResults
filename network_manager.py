import pandas as pd
import requests

class network_manager:

    @staticmethod
    def get_data(year):
        try:
            add_zero_to_year = lambda year: str(year).zfill(2)
            url = f"https://www.football-data.co.uk/mmz4281/{add_zero_to_year(year-1)}{add_zero_to_year(year)}/E0.csv"
            response = requests.get(url)

            output = open(f"data/{add_zero_to_year(year-1)}{add_zero_to_year(year)}.csv", "wb")
            output.write(response.content)
            output.close()
        except:
            print("Error")

    @staticmethod
    def get_all_years(ending_year, years):
        year_array = [ending_year - i for i in range(years)]
        for year in year_array:
            network_manager.get_data(year)