from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ValuationEntity")


@_attrs_define
class ValuationEntity:
    """
    Attributes:
        usd (float):
        asset (float):
        eth (float):
    """

    usd: float
    asset: float
    eth: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        usd = self.usd

        asset = self.asset

        eth = self.eth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "usd": usd,
                "asset": asset,
                "eth": eth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        usd = d.pop("usd")

        asset = d.pop("asset")

        eth = d.pop("eth")

        valuation_entity = cls(
            usd=usd,
            asset=asset,
            eth=eth,
        )

        valuation_entity.additional_properties = d
        return valuation_entity

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
