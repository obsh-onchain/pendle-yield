from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.point_metadata_entity_pendle_asset import PointMetadataEntityPendleAsset
from ..models.point_metadata_entity_type import PointMetadataEntityType

T = TypeVar("T", bound="PointMetadataEntity")


@_attrs_define
class PointMetadataEntity:
    """
    Attributes:
        key (str):
        type_ (PointMetadataEntityType): Either "multiplier" or "points-per-asset"
        pendle_asset (PointMetadataEntityPendleAsset): Either "basic" or "lp"
        external_dashboard_url (str):
        value (float):
        per_dollar_lp (bool):
    """

    key: str
    type_: PointMetadataEntityType
    pendle_asset: PointMetadataEntityPendleAsset
    external_dashboard_url: str
    value: float
    per_dollar_lp: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        type_ = self.type_.value

        pendle_asset = self.pendle_asset.value

        external_dashboard_url = self.external_dashboard_url

        value = self.value

        per_dollar_lp = self.per_dollar_lp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "type": type_,
                "pendleAsset": pendle_asset,
                "externalDashboardURL": external_dashboard_url,
                "value": value,
                "perDollarLp": per_dollar_lp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        type_ = PointMetadataEntityType(d.pop("type"))

        pendle_asset = PointMetadataEntityPendleAsset(d.pop("pendleAsset"))

        external_dashboard_url = d.pop("externalDashboardURL")

        value = d.pop("value")

        per_dollar_lp = d.pop("perDollarLp")

        point_metadata_entity = cls(
            key=key,
            type_=type_,
            pendle_asset=pendle_asset,
            external_dashboard_url=external_dashboard_url,
            value=value,
            per_dollar_lp=per_dollar_lp,
        )

        point_metadata_entity.additional_properties = d
        return point_metadata_entity

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
