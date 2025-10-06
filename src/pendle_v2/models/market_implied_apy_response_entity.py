from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.market_implied_apy_data_point import MarketImpliedApyDataPoint


T = TypeVar("T", bound="MarketImpliedApyResponseEntity")


@_attrs_define
class MarketImpliedApyResponseEntity:
    """
    Attributes:
        total (float):
        results (list['MarketImpliedApyDataPoint']):
        timestamp_start (Union[Unset, float]):
        timestamp_end (Union[Unset, float]):
    """

    total: float
    results: list["MarketImpliedApyDataPoint"]
    timestamp_start: Union[Unset, float] = UNSET
    timestamp_end: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        timestamp_start = self.timestamp_start

        timestamp_end = self.timestamp_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "results": results,
            }
        )
        if timestamp_start is not UNSET:
            field_dict["timestamp_start"] = timestamp_start
        if timestamp_end is not UNSET:
            field_dict["timestamp_end"] = timestamp_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market_implied_apy_data_point import MarketImpliedApyDataPoint

        d = dict(src_dict)
        total = d.pop("total")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = MarketImpliedApyDataPoint.from_dict(results_item_data)

            results.append(results_item)

        timestamp_start = d.pop("timestamp_start", UNSET)

        timestamp_end = d.pop("timestamp_end", UNSET)

        market_implied_apy_response_entity = cls(
            total=total,
            results=results,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end,
        )

        market_implied_apy_response_entity.additional_properties = d
        return market_implied_apy_response_entity

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
