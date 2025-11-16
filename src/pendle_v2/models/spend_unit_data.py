from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.valuation_entity import ValuationEntity


T = TypeVar("T", bound="SpendUnitData")


@_attrs_define
class SpendUnitData:
    """
    Attributes:
        unit (float): Balance of user in wei
        spent_v2 (ValuationEntity):
    """

    unit: float
    spent_v2: "ValuationEntity"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit = self.unit

        spent_v2 = self.spent_v2.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unit": unit,
                "spent_v2": spent_v2,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.valuation_entity import ValuationEntity

        d = dict(src_dict)
        unit = d.pop("unit")

        spent_v2 = ValuationEntity.from_dict(d.pop("spent_v2"))

        spend_unit_data = cls(
            unit=unit,
            spent_v2=spent_v2,
        )

        spend_unit_data.additional_properties = d
        return spend_unit_data

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
