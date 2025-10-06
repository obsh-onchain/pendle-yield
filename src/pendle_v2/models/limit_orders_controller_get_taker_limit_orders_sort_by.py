from enum import Enum


class LimitOrdersControllerGetTakerLimitOrdersSortBy(str, Enum):
    IMPLIED_RATE = "Implied Rate"

    def __str__(self) -> str:
        return str(self.value)
