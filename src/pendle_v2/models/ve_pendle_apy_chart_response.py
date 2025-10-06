import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.ve_pendle_apy_chart_data_point import VePendleApyChartDataPoint


T = TypeVar("T", bound="VePendleApyChartResponse")


@_attrs_define
class VePendleApyChartResponse:
    """
    Attributes:
        results (list['VePendleApyChartDataPoint']):
        time_frame (str):
        timestamp_gte (datetime.datetime):
        timestamp_lte (datetime.datetime):
    """

    results: list["VePendleApyChartDataPoint"]
    time_frame: str
    timestamp_gte: datetime.datetime
    timestamp_lte: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        time_frame = self.time_frame

        timestamp_gte = self.timestamp_gte.isoformat()

        timestamp_lte = self.timestamp_lte.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "timeFrame": time_frame,
                "timestamp_gte": timestamp_gte,
                "timestamp_lte": timestamp_lte,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ve_pendle_apy_chart_data_point import VePendleApyChartDataPoint

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = VePendleApyChartDataPoint.from_dict(results_item_data)

            results.append(results_item)

        time_frame = d.pop("timeFrame")

        timestamp_gte = isoparse(d.pop("timestamp_gte"))

        timestamp_lte = isoparse(d.pop("timestamp_lte"))

        ve_pendle_apy_chart_response = cls(
            results=results,
            time_frame=time_frame,
            timestamp_gte=timestamp_gte,
            timestamp_lte=timestamp_lte,
        )

        ve_pendle_apy_chart_response.additional_properties = d
        return ve_pendle_apy_chart_response

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
