from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VersionResponse")


@_attrs_define
class VersionResponse:
    """
    Attributes:
        major (float):
        minor (float):
        patch (float):
    """

    major: float
    minor: float
    patch: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        major = self.major

        minor = self.minor

        patch = self.patch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "major": major,
                "minor": minor,
                "patch": patch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        major = d.pop("major")

        minor = d.pop("minor")

        patch = d.pop("patch")

        version_response = cls(
            major=major,
            minor=minor,
            patch=patch,
        )

        version_response.additional_properties = d
        return version_response

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
