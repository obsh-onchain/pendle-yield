from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SyTokenOutRouteResponse")


@_attrs_define
class SyTokenOutRouteResponse:
    """
    Attributes:
        to_sy_address (str):
        default_token_out (str):
    """

    to_sy_address: str
    default_token_out: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        to_sy_address = self.to_sy_address

        default_token_out = self.default_token_out

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "toSyAddress": to_sy_address,
                "defaultTokenOut": default_token_out,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        to_sy_address = d.pop("toSyAddress")

        default_token_out = d.pop("defaultTokenOut")

        sy_token_out_route_response = cls(
            to_sy_address=to_sy_address,
            default_token_out=default_token_out,
        )

        sy_token_out_route_response.additional_properties = d
        return sy_token_out_route_response

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
