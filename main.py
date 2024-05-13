# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from command_manager import command_manager
from settings_manager import settings_manager
from data_manager import data_manager
from network_manager import network_manager

if __name__ == '__main__':
    #network_manager.get_all_years(23, 23)
    command_manager().run_program()