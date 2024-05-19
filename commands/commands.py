from .analyse import Analyse
from .command import Command
from .settings import Settings
from .teams import Teams
from .update_data import UpdateData


def get_commands() -> list[Command]:
    """
    Init all commands with their descriptions, add them to a list and return them.

    :return: commands
    """
    return [Analyse("analyse", "Create a Report with two football teams of your choice."),
            Teams("teams", "View the available teams in your selected league (Hint: change your league in settings)."),
            UpdateData("update_data", "Update all saved data manually."),
            Settings("settings", "View and change your current settings.")]
