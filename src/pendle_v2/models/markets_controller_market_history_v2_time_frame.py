from enum import Enum


class MarketsControllerMarketHistoryV2TimeFrame(str, Enum):
    DAY = "day"
    HOUR = "hour"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
