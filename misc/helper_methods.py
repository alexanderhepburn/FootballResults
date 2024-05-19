import platform
import os
import subprocess
import sys


class Colour:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class SetupProgram:
    def __init__(self):
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                              stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL)
        os.makedirs("tmp", exist_ok=True)
        os.makedirs("exports", exist_ok=True)


class SystemHandling:

    @staticmethod
    def open_file(file_name: str):
        os_name = platform.system()

        # Open the file based on the operating system
        if os_name == 'Windows':
            os.startfile(file_name)
        elif os_name == 'Darwin':  # macOS
            os.system('open ' + file_name)
        elif os_name == 'Linux':
            os.system('xdg-open ' + file_name)
        else:
            print(f"Error opening file, please open it manually!")
