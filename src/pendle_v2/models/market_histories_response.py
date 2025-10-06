import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.market_history_response import MarketHistoryResponse


T = TypeVar("T", bound="MarketHistoriesResponse")


@_attrs_define
class MarketHistoriesResponse:
    """
    Attributes:
        total (float):
        timestamp_start (datetime.datetime):
        results (list['MarketHistoryResponse']):
        limit (Union[Unset, float]):
        timestamp_end (Union[Unset, datetime.datetime]):
    """

    total: float
    timestamp_start: datetime.datetime
    results: list["MarketHistoryResponse"]
    limit: Union[Unset, float] = UNSET
    timestamp_end: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        timestamp_start = self.timestamp_start.isoformat()

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        limit = self.limit

        timestamp_end: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp_end, Unset):
            timestamp_end = self.timestamp_end.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "timestamp_start": timestamp_start,
                "results": results,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit
        if timestamp_end is not UNSET:
            field_dict["timestamp_end"] = timestamp_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market_history_response import MarketHistoryResponse

        d = dict(src_dict)
        total = d.pop("total")

        timestamp_start = isoparse(d.pop("timestamp_start"))

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = MarketHistoryResponse.from_dict(results_item_data)

            results.append(results_item)

        limit = d.pop("limit", UNSET)

        _timestamp_end = d.pop("timestamp_end", UNSET)
        timestamp_end: Union[Unset, datetime.datetime]
        if isinstance(_timestamp_end, Unset):
            timestamp_end = UNSET
        else:
            timestamp_end = isoparse(_timestamp_end)

        market_histories_response = cls(
            total=total,
            timestamp_start=timestamp_start,
            results=results,
            limit=limit,
            timestamp_end=timestamp_end,
        )

        market_histories_response.additional_properties = d
        return market_histories_response

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
