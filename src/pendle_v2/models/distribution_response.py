from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.distribution_response_rewards import DistributionResponseRewards


T = TypeVar("T", bound="DistributionResponse")


@_attrs_define
class DistributionResponse:
    """
    Attributes:
        reward_token (str): Reward token address being distributed Example: 0xE0688A2FE90d0f93F17f273235031062a210d691.
        rewards (DistributionResponseRewards): User rewards mapping Example:
            {'0x9f76a95AA7535bb0893cf88A146396e00ed21A12': {'epoch-1': {'amount': '40000000000000000000', 'timestamp':
            '1732294694'}}, '0xfdA462548Ce04282f4B6D6619823a7C64Fdc0185': {'epoch-2': {'amount': '100000000000000000000',
            'timestamp': '1741370722'}}}.
    """

    reward_token: str
    rewards: "DistributionResponseRewards"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reward_token = self.reward_token

        rewards = self.rewards.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rewardToken": reward_token,
                "rewards": rewards,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.distribution_response_rewards import DistributionResponseRewards

        d = dict(src_dict)
        reward_token = d.pop("rewardToken")

        rewards = DistributionResponseRewards.from_dict(d.pop("rewards"))

        distribution_response = cls(
            reward_token=reward_token,
            rewards=rewards,
        )

        distribution_response.additional_properties = d
        return distribution_response

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
