import os
import subprocess
import sys

from misc.colour import *
from .network_manager import download_all_data


def setup_program():
    """
    Sets up the program by installing required dependencies, creating necessary directories, and checking data.
    """

    # Install required dependencies from requirements.txt using pip
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                          stdout=subprocess.DEVNULL,  # Redirect stdout to suppress output
                          stderr=subprocess.DEVNULL)  # Redirect stderr to suppress error messages

    # Create temporary and exports directories if they don't exist
    os.makedirs("tmp", exist_ok=True)
    os.makedirs("exports", exist_ok=True)

    # Check for data directory
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Get current directory of the script
    parent_directory = os.path.dirname(current_directory)  # Get parent directory

    # Check if the data directory exists
    if not os.path.isdir(f'{parent_directory}/data'):
        print(f"{BLUE}Data upgrade required.")  # Print a message indicating data upgrade is needed
        download_all_data()
