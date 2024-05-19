from commands.command import Command
from managers.network_manager import NetworkManager


class UpdateData(Command):
    def execute(self):
        NetworkManager.get_all_data()
