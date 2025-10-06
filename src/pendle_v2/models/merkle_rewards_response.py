import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="MerkleRewardsResponse")


@_attrs_define
class MerkleRewardsResponse:
    """
    Attributes:
        accrued_amount (str):
        reward_breakdowns (Union[None, list[str]]): Only available for arbitrum-grant campaign
        updated_at (datetime.datetime):
    """

    accrued_amount: str
    reward_breakdowns: Union[None, list[str]]
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accrued_amount = self.accrued_amount

        reward_breakdowns: Union[None, list[str]]
        if isinstance(self.reward_breakdowns, list):
            reward_breakdowns = self.reward_breakdowns

        else:
            reward_breakdowns = self.reward_breakdowns

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accruedAmount": accrued_amount,
                "rewardBreakdowns": reward_breakdowns,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accrued_amount = d.pop("accruedAmount")

        def _parse_reward_breakdowns(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reward_breakdowns_type_0 = cast(list[str], data)

                return reward_breakdowns_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        reward_breakdowns = _parse_reward_breakdowns(d.pop("rewardBreakdowns"))

        updated_at = isoparse(d.pop("updatedAt"))

        merkle_rewards_response = cls(
            accrued_amount=accrued_amount,
            reward_breakdowns=reward_breakdowns,
            updated_at=updated_at,
        )

        merkle_rewards_response.additional_properties = d
        return merkle_rewards_response

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
