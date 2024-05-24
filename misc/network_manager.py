import logging
import os

import requests
from tqdm import tqdm

from misc import *
from settings import *


def download_all_data():
    """
    Downloads data for all years and leagues.

    This function fetches football data for all years and leagues, saving each dataset
    in a separate CSV file.
    """
    print(f"{GREEN}Updating data!{END}")

    accepted_leagues = [league for league in League]
    year_range = range(SettingsManager.settings_data[0].min, SettingsManager.settings_data[1].max + 1)

    total_iterations = len(year_range) * len(accepted_leagues)

    with tqdm(total=total_iterations) as pbar:
        for league in accepted_leagues:
            for year in year_range:
                try:
                    # Format the year for the required season
                    formatted_year = f"{(year % 100) - 1}{(year % 100)}"
                    url = f"https://www.football-data.co.uk/mmz4281/{formatted_year}/{league.name}.csv"

                    # Create directories if they don't exist
                    output_dir = f"data/{league.name}"
                    os.makedirs(output_dir, exist_ok=True)

                    with open(f"{output_dir}/{formatted_year}.csv", "wb") as output:
                        output.write(requests.get(url).content)  # get data and save to local file

                    # Update progress bar
                    pbar.update(1)
                except Exception as e:
                    print(f"Error in get_data: {e}")
                    logging.critical(f"Could not download data with exception: {e}")

    print(f"{GREEN}Success! Data has been updated!{END}")
