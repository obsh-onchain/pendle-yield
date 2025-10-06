from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssetDataCrossChain")


@_attrs_define
class AssetDataCrossChain:
    """
    Attributes:
        name (str): asset name Example: PT FRAX-USDC.
        decimals (float): asset decimals Example: 18.
        address (str): asset address Example: 0x5fe30ac5cb1abb0e44cdffb2916c254aeb368650.
        symbol (str): asset symbol Example: PT-FRAXUSDC_CurveLP Convex-30MAR2023.
        tags (list[str]): asset tags Example: ['PT'].
        expiry (str): asset expiry Example: 2023-03-30T00:00:00.000Z.
        pro_icon (str): asset pro icon Example: https://storage.googleapis.com/prod-pendle-
            bucket-a/images/uploads/0d3199a2-0565-4355-ad52-6bfdc67e3467.svg.
        chain_id (float): chain id Example: 1.
    """

    name: str
    decimals: float
    address: str
    symbol: str
    tags: list[str]
    expiry: str
    pro_icon: str
    chain_id: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        decimals = self.decimals

        address = self.address

        symbol = self.symbol

        tags = self.tags

        expiry = self.expiry

        pro_icon = self.pro_icon

        chain_id = self.chain_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "decimals": decimals,
                "address": address,
                "symbol": symbol,
                "tags": tags,
                "expiry": expiry,
                "proIcon": pro_icon,
                "chainId": chain_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        decimals = d.pop("decimals")

        address = d.pop("address")

        symbol = d.pop("symbol")

        tags = cast(list[str], d.pop("tags"))

        expiry = d.pop("expiry")

        pro_icon = d.pop("proIcon")

        chain_id = d.pop("chainId")

        asset_data_cross_chain = cls(
            name=name,
            decimals=decimals,
            address=address,
            symbol=symbol,
            tags=tags,
            expiry=expiry,
            pro_icon=pro_icon,
            chain_id=chain_id,
        )

        asset_data_cross_chain.additional_properties = d
        return asset_data_cross_chain

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
