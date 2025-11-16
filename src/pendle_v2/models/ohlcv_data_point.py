import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="OHLCVDataPoint")


@_attrs_define
class OHLCVDataPoint:
    """
    Attributes:
        time (datetime.datetime): Timestamp of the OHLCV data point
        open_ (float): Opening price at the start of the time period
        high (float): Highest price during the time period
        low (float): Lowest price during the time period
        close (float): Closing price at the end of the time period
        volume (float): Trading volume during the time period
    """

    time: datetime.datetime
    open_: float
    high: float
    low: float
    close: float
    volume: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time.isoformat()

        open_ = self.open_

        high = self.high

        low = self.low

        close = self.close

        volume = self.volume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time": time,
                "open": open_,
                "high": high,
                "low": low,
                "close": close,
                "volume": volume,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = isoparse(d.pop("time"))

        open_ = d.pop("open")

        high = d.pop("high")

        low = d.pop("low")

        close = d.pop("close")

        volume = d.pop("volume")

        ohlcv_data_point = cls(
            time=time,
            open_=open_,
            high=high,
            low=low,
            close=close,
            volume=volume,
        )

        ohlcv_data_point.additional_properties = d
        return ohlcv_data_point

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
