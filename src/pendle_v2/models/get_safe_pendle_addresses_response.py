from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetSafePendleAddressesResponse")


@_attrs_define
class GetSafePendleAddressesResponse:
    """
    Attributes:
        sys (list[str]): list of safe SY addresses
        pts (list[str]): list of safe PT addresses
        yts (list[str]): list of safe YT addresses
    """

    sys: list[str]
    pts: list[str]
    yts: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sys = self.sys

        pts = self.pts

        yts = self.yts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sys": sys,
                "pts": pts,
                "yts": yts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sys = cast(list[str], d.pop("sys"))

        pts = cast(list[str], d.pop("pts"))

        yts = cast(list[str], d.pop("yts"))

        get_safe_pendle_addresses_response = cls(
            sys=sys,
            pts=pts,
            yts=yts,
        )

        get_safe_pendle_addresses_response.additional_properties = d
        return get_safe_pendle_addresses_response

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
