from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.point_metadata_entity import PointMetadataEntity


T = TypeVar("T", bound="MarketPointsEntity")


@_attrs_define
class MarketPointsEntity:
    """
    Attributes:
        id (str): Market id
        points (list['PointMetadataEntity']): Points configs
    """

    id: str
    points: list["PointMetadataEntity"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()
            points.append(points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.point_metadata_entity import PointMetadataEntity

        d = dict(src_dict)
        id = d.pop("id")

        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = PointMetadataEntity.from_dict(points_item_data)

            points.append(points_item)

        market_points_entity = cls(
            id=id,
            points=points,
        )

        market_points_entity.additional_properties = d
        return market_points_entity

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
