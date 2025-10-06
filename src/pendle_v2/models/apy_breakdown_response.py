from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_basic_response import AssetBasicResponse


T = TypeVar("T", bound="ApyBreakdownResponse")


@_attrs_define
class ApyBreakdownResponse:
    """
    Attributes:
        asset (AssetBasicResponse):
        absolute_apy (float):
        relative_apy (float):
        is_external_reward (Union[None, Unset, bool]):
    """

    asset: "AssetBasicResponse"
    absolute_apy: float
    relative_apy: float
    is_external_reward: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset = self.asset.to_dict()

        absolute_apy = self.absolute_apy

        relative_apy = self.relative_apy

        is_external_reward: Union[None, Unset, bool]
        if isinstance(self.is_external_reward, Unset):
            is_external_reward = UNSET
        else:
            is_external_reward = self.is_external_reward

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset": asset,
                "absoluteApy": absolute_apy,
                "relativeApy": relative_apy,
            }
        )
        if is_external_reward is not UNSET:
            field_dict["isExternalReward"] = is_external_reward

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_basic_response import AssetBasicResponse

        d = dict(src_dict)
        asset = AssetBasicResponse.from_dict(d.pop("asset"))

        absolute_apy = d.pop("absoluteApy")

        relative_apy = d.pop("relativeApy")

        def _parse_is_external_reward(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_external_reward = _parse_is_external_reward(d.pop("isExternalReward", UNSET))

        apy_breakdown_response = cls(
            asset=asset,
            absolute_apy=absolute_apy,
            relative_apy=relative_apy,
            is_external_reward=is_external_reward,
        )

        apy_breakdown_response.additional_properties = d
        return apy_breakdown_response

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
