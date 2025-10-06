from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAssetPricesCrossChainResponsePrices")


@_attrs_define
class GetAssetPricesCrossChainResponsePrices:
    """Assets prices mapped by chainId-address

    Example:
        {'1-0x5fe30ac5cb1abb0e44cdffb2916c254aeb368650': 0.9989673642973003,
            '1-0xd393d1ddd6b8811a86d925f5e14014282581bc04': 1.001712}

    """

    additional_properties: dict[str, float] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        get_asset_prices_cross_chain_response_prices = cls()

        get_asset_prices_cross_chain_response_prices.additional_properties = d
        return get_asset_prices_cross_chain_response_prices

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> float:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: float) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
