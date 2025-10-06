from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.supported_aggregator import SupportedAggregator


T = TypeVar("T", bound="SupportedAggregatorsResponse")


@_attrs_define
class SupportedAggregatorsResponse:
    """
    Attributes:
        aggregators (list['SupportedAggregator']): List of supported aggregators with their computing units
    """

    aggregators: list["SupportedAggregator"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregators = []
        for aggregators_item_data in self.aggregators:
            aggregators_item = aggregators_item_data.to_dict()
            aggregators.append(aggregators_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aggregators": aggregators,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.supported_aggregator import SupportedAggregator

        d = dict(src_dict)
        aggregators = []
        _aggregators = d.pop("aggregators")
        for aggregators_item_data in _aggregators:
            aggregators_item = SupportedAggregator.from_dict(aggregators_item_data)

            aggregators.append(aggregators_item)

        supported_aggregators_response = cls(
            aggregators=aggregators,
        )

        supported_aggregators_response.additional_properties = d
        return supported_aggregators_response

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
