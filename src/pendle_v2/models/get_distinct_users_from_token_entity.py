from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetDistinctUsersFromTokenEntity")


@_attrs_define
class GetDistinctUsersFromTokenEntity:
    """
    Attributes:
        users (list[str]): Array of unique wallet addresses (lowercase) that have interacted with the specified token.
            Addresses are deduplicated across both Sentio and internal data sources. Example:
            ['0x1234567890123456789012345678901234567890', '0x0987654321098765432109876543210987654321',
            '0xabcdefabcdefabcdefabcdefabcdefabcdefabcd'].
    """

    users: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users = self.users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "users": users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        users = cast(list[str], d.pop("users"))

        get_distinct_users_from_token_entity = cls(
            users=users,
        )

        get_distinct_users_from_token_entity.additional_properties = d
        return get_distinct_users_from_token_entity

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
