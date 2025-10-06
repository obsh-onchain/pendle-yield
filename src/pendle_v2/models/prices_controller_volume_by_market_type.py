from enum import Enum


class PricesControllerVolumeByMarketType(str, Enum):
    PT = "pt"
    YT = "yt"

    def __str__(self) -> str:
        return str(self.value)
