from commands.command import Command
from network_manager import network_manager


class UpdateData(Command):
    def execute(self):
        network_manager.get_all_data()
