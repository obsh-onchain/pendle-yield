from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EulerUserResponse")


@_attrs_define
class EulerUserResponse:
    """
    Attributes:
        user (str): Euler user address
        sub_account (str): Euler sub account address
        asset (str): Euler vault address
    """

    user: str
    sub_account: str
    asset: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user

        sub_account = self.sub_account

        asset = self.asset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "subAccount": sub_account,
                "asset": asset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user = d.pop("user")

        sub_account = d.pop("subAccount")

        asset = d.pop("asset")

        euler_user_response = cls(
            user=user,
            sub_account=sub_account,
            asset=asset,
        )

        euler_user_response.additional_properties = d
        return euler_user_response

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
