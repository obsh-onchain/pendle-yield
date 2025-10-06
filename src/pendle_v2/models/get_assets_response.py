from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.asset_data import AssetData


T = TypeVar("T", bound="GetAssetsResponse")


@_attrs_define
class GetAssetsResponse:
    """
    Attributes:
        assets (list['AssetData']): list of assets Example: [{'name': 'PT FRAX-USDC', 'decimals': 18, 'address':
            '0x5fe30ac5cb1abb0e44cdffb2916c254aeb368650', 'symbol': 'PT-FRAXUSDC_CurveLP Convex-30MAR2023', 'tags': ['PT'],
            'expiry': '2023-03-30T00:00:00.000Z', 'proIcon': 'https://storage.googleapis.com/prod-pendle-
            bucket-a/images/assets/pro/acad6337-8ce4-47c2-87a7-c270aab01b3d.svg'}, {'name': 'YT FRAX-USDC', 'decimals': 18,
            'address': '0xc5cd692e9b4622ab8cdb57c83a0f99f874a169cd', 'symbol': 'YT-FRAXUSDC_CurveLP Convex-30MAR2023',
            'tags': ['YT'], 'expiry': '2023-03-30T00:00:00.000Z', 'proIcon': 'https://storage.googleapis.com/prod-pendle-
            bucket-a/images/assets/pro/2239e536-439d-4c58-a417-805fb63c7ced.svg'}].
    """

    assets: list["AssetData"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets = []
        for assets_item_data in self.assets:
            assets_item = assets_item_data.to_dict()
            assets.append(assets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assets": assets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_data import AssetData

        d = dict(src_dict)
        assets = []
        _assets = d.pop("assets")
        for assets_item_data in _assets:
            assets_item = AssetData.from_dict(assets_item_data)

            assets.append(assets_item)

        get_assets_response = cls(
            assets=assets,
        )

        get_assets_response.additional_properties = d
        return get_assets_response

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
