from enum import Enum


class PendleAssetType(str, Enum):
    PENDLE_LP = "PENDLE_LP"
    PT = "PT"
    SY = "SY"
    YT = "YT"

    def __str__(self) -> str:
        return str(self.value)
