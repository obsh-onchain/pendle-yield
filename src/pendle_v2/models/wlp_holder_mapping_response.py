from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WlpHolderMappingResponse")


@_attrs_define
class WlpHolderMappingResponse:
    """
    Attributes:
        holder (str): The address of the holder
        asset (str): The address of the asset
        money_market (str): The address of the money market
    """

    holder: str
    asset: str
    money_market: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        holder = self.holder

        asset = self.asset

        money_market = self.money_market

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "holder": holder,
                "asset": asset,
                "moneyMarket": money_market,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        holder = d.pop("holder")

        asset = d.pop("asset")

        money_market = d.pop("moneyMarket")

        wlp_holder_mapping_response = cls(
            holder=holder,
            asset=asset,
            money_market=money_market,
        )

        wlp_holder_mapping_response.additional_properties = d
        return wlp_holder_mapping_response

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
