from enum import Enum


class LimitOrderResponseStatus(str, Enum):
    CANCELLED = "CANCELLED"
    EMPTY_MAKER_BALANCE = "EMPTY_MAKER_BALANCE"
    EXPIRED = "EXPIRED"
    FAILED_TRANSFER_TOKEN = "FAILED_TRANSFER_TOKEN"
    FILLABLE = "FILLABLE"
    FULLY_FILLED = "FULLY_FILLED"
    PARTIAL_FILLABLE = "PARTIAL_FILLABLE"

    def __str__(self) -> str:
        return str(self.value)
