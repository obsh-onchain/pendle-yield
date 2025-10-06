from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SupportedAggregator")


@_attrs_define
class SupportedAggregator:
    """
    Attributes:
        name (str): Name of the aggregator, e.g., kyberswap, okx, odos, paraswap Example: kyberswap.
        computing_unit (float): Computing unit required for the aggregator Example: 5.
    """

    name: str
    computing_unit: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        computing_unit = self.computing_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "computingUnit": computing_unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        computing_unit = d.pop("computingUnit")

        supported_aggregator = cls(
            name=name,
            computing_unit=computing_unit,
        )

        supported_aggregator.additional_properties = d
        return supported_aggregator

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
