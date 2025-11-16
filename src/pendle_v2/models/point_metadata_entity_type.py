from enum import Enum


class PointMetadataEntityType(str, Enum):
    MULTIPLIER = "multiplier"
    POINTS_PER_ASSET = "points-per-asset"

    def __str__(self) -> str:
        return str(self.value)
