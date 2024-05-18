import platform
import os


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
