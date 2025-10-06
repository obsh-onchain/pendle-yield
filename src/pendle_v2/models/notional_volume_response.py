from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NotionalVolumeResponse")


@_attrs_define
class NotionalVolumeResponse:
    """
    Attributes:
        timestamps (list[str]): List of timestamps, each will be mapped to a notional volume
        volumes (list[float]): List of notional volumes corresponding to each timestamp. It has the same length with
            timestamps array
    """

    timestamps: list[str]
    volumes: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamps = self.timestamps

        volumes = self.volumes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamps": timestamps,
                "volumes": volumes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamps = cast(list[str], d.pop("timestamps"))

        volumes = cast(list[float], d.pop("volumes"))

        notional_volume_response = cls(
            timestamps=timestamps,
            volumes=volumes,
        )

        notional_volume_response.additional_properties = d
        return notional_volume_response

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
