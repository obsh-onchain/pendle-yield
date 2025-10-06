from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.integration_asset_entity import IntegrationAssetEntity


T = TypeVar("T", bound="IntegrationAssetResponse")


@_attrs_define
class IntegrationAssetResponse:
    """
    Attributes:
        asset (IntegrationAssetEntity):
    """

    asset: "IntegrationAssetEntity"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset = self.asset.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset": asset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_asset_entity import IntegrationAssetEntity

        d = dict(src_dict)
        asset = IntegrationAssetEntity.from_dict(d.pop("asset"))

        integration_asset_response = cls(
            asset=asset,
        )

        integration_asset_response.additional_properties = d
        return integration_asset_response

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
