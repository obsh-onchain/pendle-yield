from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetLiquidityTransferableMarketsResponse")


@_attrs_define
class GetLiquidityTransferableMarketsResponse:
    """
    Attributes:
        market_addresses (list[str]): list of liquidity transferable markets
    """

    market_addresses: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        market_addresses = self.market_addresses

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketAddresses": market_addresses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        market_addresses = cast(list[str], d.pop("marketAddresses"))

        get_liquidity_transferable_markets_response = cls(
            market_addresses=market_addresses,
        )

        get_liquidity_transferable_markets_response.additional_properties = d
        return get_liquidity_transferable_markets_response

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
