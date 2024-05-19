from commands.command import Command
from misc import get_all_data


class UpdateData(Command):
    def execute(self):
        get_all_data()
