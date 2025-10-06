from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PairEntity")


@_attrs_define
class PairEntity:
    """
    Attributes:
        id (str): Pendle LPT address
        dex_key (str): Dex key. Result is always pendle. Example: pendle.
        asset_0_id (str): PT address
        asset_1_id (str): SY address
    """

    id: str
    dex_key: str
    asset_0_id: str
    asset_1_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        dex_key = self.dex_key

        asset_0_id = self.asset_0_id

        asset_1_id = self.asset_1_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "dexKey": dex_key,
                "asset0Id": asset_0_id,
                "asset1Id": asset_1_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        dex_key = d.pop("dexKey")

        asset_0_id = d.pop("asset0Id")

        asset_1_id = d.pop("asset1Id")

        pair_entity = cls(
            id=id,
            dex_key=dex_key,
            asset_0_id=asset_0_id,
            asset_1_id=asset_1_id,
        )

        pair_entity.additional_properties = d
        return pair_entity

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
