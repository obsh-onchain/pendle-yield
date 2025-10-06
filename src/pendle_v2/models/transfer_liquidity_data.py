from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TransferLiquidityData")


@_attrs_define
class TransferLiquidityData:
    """
    Attributes:
        amount_lp_out (str):
        amount_yt_out (str):
        price_impact (float):
    """

    amount_lp_out: str
    amount_yt_out: str
    price_impact: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_lp_out = self.amount_lp_out

        amount_yt_out = self.amount_yt_out

        price_impact = self.price_impact

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amountLpOut": amount_lp_out,
                "amountYtOut": amount_yt_out,
                "priceImpact": price_impact,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_lp_out = d.pop("amountLpOut")

        amount_yt_out = d.pop("amountYtOut")

        price_impact = d.pop("priceImpact")

        transfer_liquidity_data = cls(
            amount_lp_out=amount_lp_out,
            amount_yt_out=amount_yt_out,
            price_impact=price_impact,
        )

        transfer_liquidity_data.additional_properties = d
        return transfer_liquidity_data

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
