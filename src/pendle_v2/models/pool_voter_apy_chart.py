from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pool_response import PoolResponse
    from ..models.voter_apy_chart_data_point import VoterApyChartDataPoint


T = TypeVar("T", bound="PoolVoterApyChart")


@_attrs_define
class PoolVoterApyChart:
    """
    Attributes:
        values (list['VoterApyChartDataPoint']):
        pool (PoolResponse):
    """

    values: list["VoterApyChartDataPoint"]
    pool: "PoolResponse"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        pool = self.pool.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "values": values,
                "pool": pool,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pool_response import PoolResponse
        from ..models.voter_apy_chart_data_point import VoterApyChartDataPoint

        d = dict(src_dict)
        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = VoterApyChartDataPoint.from_dict(values_item_data)

            values.append(values_item)

        pool = PoolResponse.from_dict(d.pop("pool"))

        pool_voter_apy_chart = cls(
            values=values,
            pool=pool,
        )

        pool_voter_apy_chart.additional_properties = d
        return pool_voter_apy_chart

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
