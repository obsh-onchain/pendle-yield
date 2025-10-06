from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.asset_basic_response import AssetBasicResponse


T = TypeVar("T", bound="EstimatedDailyPoolRewardResponse")


@_attrs_define
class EstimatedDailyPoolRewardResponse:
    """
    Attributes:
        asset (AssetBasicResponse):
        amount (float):
    """

    asset: "AssetBasicResponse"
    amount: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset = self.asset.to_dict()

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset": asset,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_basic_response import AssetBasicResponse

        d = dict(src_dict)
        asset = AssetBasicResponse.from_dict(d.pop("asset"))

        amount = d.pop("amount")

        estimated_daily_pool_reward_response = cls(
            asset=asset,
            amount=amount,
        )

        estimated_daily_pool_reward_response.additional_properties = d
        return estimated_daily_pool_reward_response

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
