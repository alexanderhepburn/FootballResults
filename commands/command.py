from abc import ABC, abstractmethod


class Command(ABC):

    def __init__(self, command_name: str, command_description: str):
        self.command_name = command_name
        self.command_description = command_description

        @abstractmethod
        def execute(self) -> None:
            pass
