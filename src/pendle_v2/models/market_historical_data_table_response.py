from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MarketHistoricalDataTableResponse")


@_attrs_define
class MarketHistoricalDataTableResponse:
    """
    Attributes:
        total (float):
        timestamp_start (float):
        timestamp_end (float):
        timestamp (list[float]): Array of timestamp in second
        max_apy (list[float]): Array of maxApy. 0.5 means 50%
        base_apy (list[float]): Array of baseApy. 0.5 means 50%
        underlying_apy (list[float]): Array of underlyingApy. 0.5 means 50%
        implied_apy (list[float]): Array of impliedApy. 0.5 means 50%
        tvl (list[float]): Array of tvl
    """

    total: float
    timestamp_start: float
    timestamp_end: float
    timestamp: list[float]
    max_apy: list[float]
    base_apy: list[float]
    underlying_apy: list[float]
    implied_apy: list[float]
    tvl: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        timestamp_start = self.timestamp_start

        timestamp_end = self.timestamp_end

        timestamp = self.timestamp

        max_apy = self.max_apy

        base_apy = self.base_apy

        underlying_apy = self.underlying_apy

        implied_apy = self.implied_apy

        tvl = self.tvl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "timestamp_start": timestamp_start,
                "timestamp_end": timestamp_end,
                "timestamp": timestamp,
                "maxApy": max_apy,
                "baseApy": base_apy,
                "underlyingApy": underlying_apy,
                "impliedApy": implied_apy,
                "tvl": tvl,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        timestamp_start = d.pop("timestamp_start")

        timestamp_end = d.pop("timestamp_end")

        timestamp = cast(list[float], d.pop("timestamp"))

        max_apy = cast(list[float], d.pop("maxApy"))

        base_apy = cast(list[float], d.pop("baseApy"))

        underlying_apy = cast(list[float], d.pop("underlyingApy"))

        implied_apy = cast(list[float], d.pop("impliedApy"))

        tvl = cast(list[float], d.pop("tvl"))

        market_historical_data_table_response = cls(
            total=total,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end,
            timestamp=timestamp,
            max_apy=max_apy,
            base_apy=base_apy,
            underlying_apy=underlying_apy,
            implied_apy=implied_apy,
            tvl=tvl,
        )

        market_historical_data_table_response.additional_properties = d
        return market_historical_data_table_response

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
