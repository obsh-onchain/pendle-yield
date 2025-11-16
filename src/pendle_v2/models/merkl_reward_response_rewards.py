from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MerklRewardResponseRewards")


@_attrs_define
class MerklRewardResponseRewards:
    """User rewards mapping

    Example:
        {'0x9f76a95AA7535bb0893cf88A146396e00ed21A12': {'epoch-1': {'amount': '40000000000000000000', 'timestamp':
            '1732294694'}}, '0xfdA462548Ce04282f4B6D6619823a7C64Fdc0185': {'epoch-2': {'amount': '100000000000000000000',
            'timestamp': '1741370722'}}}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        merkl_reward_response_rewards = cls()

        merkl_reward_response_rewards.additional_properties = d
        return merkl_reward_response_rewards

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
