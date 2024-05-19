from abc import ABC, abstractmethod


class Command(ABC):
    """
    Abstract base class for commands.

    Attributes:
        command_name (str): The name of the command.
        command_description (str): The description of the command.
    """

    def __init__(self, command_name: str, command_description: str):
        """
        Initializes the Command object with a name and description.

        Args:
            command_name (str): The name of the command.
            command_description (str): The description of the command.
        """
        self.command_name = command_name
        self.command_description = command_description

    @abstractmethod
    def execute(self) -> None:
        """
        Abstract method to execute the command.
        This method must be implemented by subclasses.
        """
        pass
