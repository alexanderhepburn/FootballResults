from commands.analyse import Analyse
from commands.teams import Teams
from commands.update_data import UpdateData
from commands.settings import Settings


class Commands:
    commands = [Analyse("analyse", "Analyse two teams."),
                Teams("teams", "TO DO"),
                UpdateData("update_data", "TO DO"),
                Settings("settings", "TO DO")]
