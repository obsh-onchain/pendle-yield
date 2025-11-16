import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="MarketApyHistoryResponse")


@_attrs_define
class MarketApyHistoryResponse:
    """
    Attributes:
        timestamp (datetime.datetime): Timestamp of the APY data point
        underlying_apy (float): APY of the underlying asset
        implied_apy (float): Implied APY of market
    """

    timestamp: datetime.datetime
    underlying_apy: float
    implied_apy: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        underlying_apy = self.underlying_apy

        implied_apy = self.implied_apy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "underlyingApy": underlying_apy,
                "impliedApy": implied_apy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = isoparse(d.pop("timestamp"))

        underlying_apy = d.pop("underlyingApy")

        implied_apy = d.pop("impliedApy")

        market_apy_history_response = cls(
            timestamp=timestamp,
            underlying_apy=underlying_apy,
            implied_apy=implied_apy,
        )

        market_apy_history_response.additional_properties = d
        return market_apy_history_response

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
