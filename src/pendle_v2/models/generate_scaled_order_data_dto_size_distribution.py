from enum import Enum


class GenerateScaledOrderDataDtoSizeDistribution(str, Enum):
    ASCENDING = "ascending"
    DESCENDING = "descending"
    FLAT = "flat"

    def __str__(self) -> str:
        return str(self.value)
