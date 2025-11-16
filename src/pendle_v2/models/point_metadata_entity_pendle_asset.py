from enum import Enum


class PointMetadataEntityPendleAsset(str, Enum):
    BASIC = "basic"
    LP = "lp"

    def __str__(self) -> str:
        return str(self.value)
