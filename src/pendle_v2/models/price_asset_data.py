from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PriceAssetData")


@_attrs_define
class PriceAssetData:
    """
    Attributes:
        pt (float):
        yt (float):
        lp (float):
    """

    pt: float
    yt: float
    lp: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pt = self.pt

        yt = self.yt

        lp = self.lp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pt": pt,
                "yt": yt,
                "lp": lp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pt = d.pop("pt")

        yt = d.pop("yt")

        lp = d.pop("lp")

        price_asset_data = cls(
            pt=pt,
            yt=yt,
            lp=lp,
        )

        price_asset_data.additional_properties = d
        return price_asset_data

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
