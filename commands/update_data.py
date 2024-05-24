from commands.command import Command
from misc import download_all_data


class UpdateData(Command):
    """
    Command to update all data by downloading it from the source.
    """

    def execute(self):
        """
        Executes the update data command, calling the get_all_data function.
        """
        # Call the function to download and update all data
        download_all_data()
