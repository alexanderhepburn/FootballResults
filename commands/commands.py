from .analyse import Analyse
from .teams import Teams
from .update_data import UpdateData
from .settings import Settings
from .command import Command


def get_commands() -> list[Command]:
    return [Analyse("analyse", "Analyse two teams."),
            Teams("teams", "TO DO"),
            UpdateData("update_data", "TO DO"),
            Settings("settings", "TO DO")]
