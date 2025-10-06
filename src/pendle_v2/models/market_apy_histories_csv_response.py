from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MarketApyHistoriesCSVResponse")


@_attrs_define
class MarketApyHistoriesCSVResponse:
    """
    Attributes:
        total (float):
        timestamp_start (float):
        timestamp_end (float):
        results (str):
    """

    total: float
    timestamp_start: float
    timestamp_end: float
    results: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        timestamp_start = self.timestamp_start

        timestamp_end = self.timestamp_end

        results = self.results

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "timestamp_start": timestamp_start,
                "timestamp_end": timestamp_end,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        timestamp_start = d.pop("timestamp_start")

        timestamp_end = d.pop("timestamp_end")

        results = d.pop("results")

        market_apy_histories_csv_response = cls(
            total=total,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end,
            results=results,
        )

        market_apy_histories_csv_response.additional_properties = d
        return market_apy_histories_csv_response

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
