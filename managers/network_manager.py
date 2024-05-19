import logging
import os

import requests
from tqdm import tqdm

from misc.helper_methods import Colour
from settings.league import League
from settings.settings_manager import SettingsManager


class NetworkManager:
    """
    A utility class for managing network operations related to fetching and updating football data.

    This class provides methods for downloading data for specific years and leagues,
    updating data for all available years and leagues, and setting up the network manager.

    Attributes:
        None
    """

    @staticmethod
    def get_data(year, league):
        """
        Downloads data for a specific year and league from a URL and saves it to a file.

        Args:
            year (int): The year for which data is to be downloaded.
            league (League): The league for which data is to be downloaded.
        """
        try:
            formatted_year = f"{(year % 100) - 1}{(year % 100)}"  # Format the year for the required season
            url = f"https://www.football-data.co.uk/mmz4281/{formatted_year}/{league.name}.csv"
            response = requests.get(url)

            os.makedirs(f"data/{league.name}", exist_ok=True)  # Create directories if they don't exist

            with open(f"data/{league.name}/{formatted_year}.csv", "wb") as output:
                output.write(response.content)  # save the data to the local file
        except Exception as e:
            print(f"Error in get_data: {e}")
            logging.critical(f"Could not download data with exception: {e}")

    @staticmethod
    def get_all_data():
        """Downloads data for all years and leagues."""
        print(f"{Colour.GREEN}Updating data!{Colour.END}")

        accepted_leagues = [league for league in League]  # Get the list of accepted leagues
        year_array = list(range(SettingsManager.settings_data[0].min,
                                SettingsManager.settings_data[1].max + 1))  # Get the range of years to fetch data for
        total_iterations = len(year_array) * len(accepted_leagues)

        with tqdm(total=total_iterations) as pbar:
            for league in accepted_leagues:
                for year in year_array:
                    # Fetch data for each year and league
                    NetworkManager.get_data(year, league)
                    pbar.update(1)
        print(f"{Colour.GREEN}Success! Data has been updated!{Colour.END}")

    @staticmethod
    def setup():
        """Sets up the network manager."""
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)

        # Check if the data directory exists
        if not os.path.isdir(f'{parent_directory}/data'):
            print(f"{Colour.BLUE}Data upgrade required.")
            NetworkManager.get_all_data()  # If not, upgrade data
