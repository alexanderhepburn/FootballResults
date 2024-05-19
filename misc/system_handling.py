import os
import platform


def open_file(file_name: str):
    """
    Opens the specified file using the default application associated with its file type.

    Args:
        file_name (str): The name of the file to be opened.
    """
    os_name = platform.system()  # Get the name of the current operating system

    # Open the file based on the operating system
    if os_name == 'Windows':
        os.startfile(file_name)  # Open file using default Windows application
    elif os_name == 'Darwin':  # macOS
        os.system('open ' + file_name)  # Open file using 'open' command in macOS
    elif os_name == 'Linux':
        os.system('xdg-open ' + file_name)  # Open file using 'xdg-open' command in Linux
    else:
        # If the operating system is not recognized, print an error message
        print(f"Error opening file '{file_name}': Unsupported operating system!")
