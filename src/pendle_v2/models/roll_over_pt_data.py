from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RollOverPtData")


@_attrs_define
class RollOverPtData:
    """
    Attributes:
        amount_pt_out (str):
        price_impact (float):
    """

    amount_pt_out: str
    price_impact: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_pt_out = self.amount_pt_out

        price_impact = self.price_impact

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amountPtOut": amount_pt_out,
                "priceImpact": price_impact,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_pt_out = d.pop("amountPtOut")

        price_impact = d.pop("priceImpact")

        roll_over_pt_data = cls(
            amount_pt_out=amount_pt_out,
            price_impact=price_impact,
        )

        roll_over_pt_data.additional_properties = d
        return roll_over_pt_data

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
