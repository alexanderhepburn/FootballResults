import os
import subprocess
import sys

from misc.colour import *
from .network_manager import get_all_data


def setup_program():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                          stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL)
    os.makedirs("tmp", exist_ok=True)
    os.makedirs("exports", exist_ok=True)

    # Check for data
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)

    # Check if the data directory exists
    if not os.path.isdir(f'{parent_directory}/data'):
        print(f"{BLUE}Data upgrade required.")
        get_all_data()  # If not, upgrade data
