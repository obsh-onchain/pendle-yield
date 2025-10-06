from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.implied_apy import ImpliedApy


T = TypeVar("T", bound="RemoveLiquidityData")


@_attrs_define
class RemoveLiquidityData:
    """
    Attributes:
        amount_out (str):
        price_impact (float):
        implied_apy (Union[Unset, ImpliedApy]):
    """

    amount_out: str
    price_impact: float
    implied_apy: Union[Unset, "ImpliedApy"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_out = self.amount_out

        price_impact = self.price_impact

        implied_apy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.implied_apy, Unset):
            implied_apy = self.implied_apy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amountOut": amount_out,
                "priceImpact": price_impact,
            }
        )
        if implied_apy is not UNSET:
            field_dict["impliedApy"] = implied_apy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.implied_apy import ImpliedApy

        d = dict(src_dict)
        amount_out = d.pop("amountOut")

        price_impact = d.pop("priceImpact")

        _implied_apy = d.pop("impliedApy", UNSET)
        implied_apy: Union[Unset, ImpliedApy]
        if isinstance(_implied_apy, Unset):
            implied_apy = UNSET
        else:
            implied_apy = ImpliedApy.from_dict(_implied_apy)

        remove_liquidity_data = cls(
            amount_out=amount_out,
            price_impact=price_impact,
            implied_apy=implied_apy,
        )

        remove_liquidity_data.additional_properties = d
        return remove_liquidity_data

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
