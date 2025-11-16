from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.merkle_user_campaign_response import MerkleUserCampaignResponse


T = TypeVar("T", bound="MerkleClaimableRewardsResponse")


@_attrs_define
class MerkleClaimableRewardsResponse:
    """
    Attributes:
        claimable_rewards (list['MerkleUserCampaignResponse']): Array of unclaimed merkle campaigns
    """

    claimable_rewards: list["MerkleUserCampaignResponse"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        claimable_rewards = []
        for claimable_rewards_item_data in self.claimable_rewards:
            claimable_rewards_item = claimable_rewards_item_data.to_dict()
            claimable_rewards.append(claimable_rewards_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "claimableRewards": claimable_rewards,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.merkle_user_campaign_response import MerkleUserCampaignResponse

        d = dict(src_dict)
        claimable_rewards = []
        _claimable_rewards = d.pop("claimableRewards")
        for claimable_rewards_item_data in _claimable_rewards:
            claimable_rewards_item = MerkleUserCampaignResponse.from_dict(claimable_rewards_item_data)

            claimable_rewards.append(claimable_rewards_item)

        merkle_claimable_rewards_response = cls(
            claimable_rewards=claimable_rewards,
        )

        merkle_claimable_rewards_response.additional_properties = d
        return merkle_claimable_rewards_response

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
