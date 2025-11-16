from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.merkl_reward_response_rewards import MerklRewardResponseRewards


T = TypeVar("T", bound="MerklRewardResponse")


@_attrs_define
class MerklRewardResponse:
    """
    Attributes:
        sum_amount (str): Chain ID Example: 1.
        from_epoch (float): From epoch Example: 1732294694.
        to_epoch (float): To epoch Example: 1732294694.
        hash_ (str): Hash of the distribution file Example: 0x1234567890abcdef.
        reward_token (str): Reward token address being distributed Example: 0xE0688A2FE90d0f93F17f273235031062a210d691.
        rewards (MerklRewardResponseRewards): User rewards mapping Example:
            {'0x9f76a95AA7535bb0893cf88A146396e00ed21A12': {'epoch-1': {'amount': '40000000000000000000', 'timestamp':
            '1732294694'}}, '0xfdA462548Ce04282f4B6D6619823a7C64Fdc0185': {'epoch-2': {'amount': '100000000000000000000',
            'timestamp': '1741370722'}}}.
    """

    sum_amount: str
    from_epoch: float
    to_epoch: float
    hash_: str
    reward_token: str
    rewards: "MerklRewardResponseRewards"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sum_amount = self.sum_amount

        from_epoch = self.from_epoch

        to_epoch = self.to_epoch

        hash_ = self.hash_

        reward_token = self.reward_token

        rewards = self.rewards.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sumAmount": sum_amount,
                "fromEpoch": from_epoch,
                "toEpoch": to_epoch,
                "hash": hash_,
                "rewardToken": reward_token,
                "rewards": rewards,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.merkl_reward_response_rewards import MerklRewardResponseRewards

        d = dict(src_dict)
        sum_amount = d.pop("sumAmount")

        from_epoch = d.pop("fromEpoch")

        to_epoch = d.pop("toEpoch")

        hash_ = d.pop("hash")

        reward_token = d.pop("rewardToken")

        rewards = MerklRewardResponseRewards.from_dict(d.pop("rewards"))

        merkl_reward_response = cls(
            sum_amount=sum_amount,
            from_epoch=from_epoch,
            to_epoch=to_epoch,
            hash_=hash_,
            reward_token=reward_token,
            rewards=rewards,
        )

        merkl_reward_response.additional_properties = d
        return merkl_reward_response

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
