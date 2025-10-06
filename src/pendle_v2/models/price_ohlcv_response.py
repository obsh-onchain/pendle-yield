import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ohlcv_data_point import OHLCVDataPoint


T = TypeVar("T", bound="PriceOHLCVResponse")


@_attrs_define
class PriceOHLCVResponse:
    """
    Attributes:
        limit (float):
        total (float):
        currency (str):
        time_frame (str):
        results (list['OHLCVDataPoint']):
        timestamp_start (Union[Unset, datetime.datetime]):
        timestamp_end (Union[Unset, datetime.datetime]):
    """

    limit: float
    total: float
    currency: str
    time_frame: str
    results: list["OHLCVDataPoint"]
    timestamp_start: Union[Unset, datetime.datetime] = UNSET
    timestamp_end: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        total = self.total

        currency = self.currency

        time_frame = self.time_frame

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        timestamp_start: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp_start, Unset):
            timestamp_start = self.timestamp_start.isoformat()

        timestamp_end: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp_end, Unset):
            timestamp_end = self.timestamp_end.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
                "total": total,
                "currency": currency,
                "timeFrame": time_frame,
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
        from ..models.ohlcv_data_point import OHLCVDataPoint

        d = dict(src_dict)
        limit = d.pop("limit")

        total = d.pop("total")

        currency = d.pop("currency")

        time_frame = d.pop("timeFrame")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = OHLCVDataPoint.from_dict(results_item_data)

            results.append(results_item)

        _timestamp_start = d.pop("timestamp_start", UNSET)
        timestamp_start: Union[Unset, datetime.datetime]
        if isinstance(_timestamp_start, Unset):
            timestamp_start = UNSET
        else:
            timestamp_start = isoparse(_timestamp_start)

        _timestamp_end = d.pop("timestamp_end", UNSET)
        timestamp_end: Union[Unset, datetime.datetime]
        if isinstance(_timestamp_end, Unset):
            timestamp_end = UNSET
        else:
            timestamp_end = isoparse(_timestamp_end)

        price_ohlcv_response = cls(
            limit=limit,
            total=total,
            currency=currency,
            time_frame=time_frame,
            results=results,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end,
        )

        price_ohlcv_response.additional_properties = d
        return price_ohlcv_response

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
