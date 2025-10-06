from enum import Enum


class SwapEventEventType(str, Enum):
    EXIT = "exit"
    JOIN = "join"
    SWAP = "swap"

    def __str__(self) -> str:
        return str(self.value)
