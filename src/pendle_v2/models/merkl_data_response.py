from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MerklDataResponse")


@_attrs_define
class MerklDataResponse:
    """
    Attributes:
        tvl (str): Total Value Locked as a string Example: 1000000000000000000000.
        apr (str): Annual Percentage Rate in decimal format Example: 0.15.
        opportunity_name (Union[Unset, str]): Optional opportunity name Example: Pendle Market Maker Incentive.
    """

    tvl: str
    apr: str
    opportunity_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tvl = self.tvl

        apr = self.apr

        opportunity_name = self.opportunity_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tvl": tvl,
                "apr": apr,
            }
        )
        if opportunity_name is not UNSET:
            field_dict["opportunityName"] = opportunity_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tvl = d.pop("tvl")

        apr = d.pop("apr")

        opportunity_name = d.pop("opportunityName", UNSET)

        merkl_data_response = cls(
            tvl=tvl,
            apr=apr,
            opportunity_name=opportunity_name,
        )

        merkl_data_response.additional_properties = d
        return merkl_data_response

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
