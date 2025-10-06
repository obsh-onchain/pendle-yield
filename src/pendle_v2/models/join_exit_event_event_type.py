from enum import Enum


class JoinExitEventEventType(str, Enum):
    EXIT = "exit"
    JOIN = "join"
    SWAP = "swap"

    def __str__(self) -> str:
        return str(self.value)
