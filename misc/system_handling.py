import os
import platform


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
