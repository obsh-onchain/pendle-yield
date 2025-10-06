from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LiquidLockerPoolResponse")


@_attrs_define
class LiquidLockerPoolResponse:
    """
    Attributes:
        name (str):
        lp_holder (str):
        receipt_token (str):
        users (list[str]):
        error_message (str):
    """

    name: str
    lp_holder: str
    receipt_token: str
    users: list[str]
    error_message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        lp_holder = self.lp_holder

        receipt_token = self.receipt_token

        users = self.users

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "lpHolder": lp_holder,
                "receiptToken": receipt_token,
                "users": users,
                "errorMessage": error_message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        lp_holder = d.pop("lpHolder")

        receipt_token = d.pop("receiptToken")

        users = cast(list[str], d.pop("users"))

        error_message = d.pop("errorMessage")

        liquid_locker_pool_response = cls(
            name=name,
            lp_holder=lp_holder,
            receipt_token=receipt_token,
            users=users,
            error_message=error_message,
        )

        liquid_locker_pool_response.additional_properties = d
        return liquid_locker_pool_response

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
