from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.curreny_amount_entity import CurrenyAmountEntity


T = TypeVar("T", bound="FeaturedMarketEntity")


@_attrs_define
class FeaturedMarketEntity:
    """
    Attributes:
        market_address (str):
        icon (str):
        token_symbol (str):
        symbol (str):
        accent_color (str):
        discounted_price (CurrenyAmountEntity):
        fixed_apy (float):
        current_price (CurrenyAmountEntity):
    """

    market_address: str
    icon: str
    token_symbol: str
    symbol: str
    accent_color: str
    discounted_price: "CurrenyAmountEntity"
    fixed_apy: float
    current_price: "CurrenyAmountEntity"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        market_address = self.market_address

        icon = self.icon

        token_symbol = self.token_symbol

        symbol = self.symbol

        accent_color = self.accent_color

        discounted_price = self.discounted_price.to_dict()

        fixed_apy = self.fixed_apy

        current_price = self.current_price.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketAddress": market_address,
                "icon": icon,
                "tokenSymbol": token_symbol,
                "symbol": symbol,
                "accentColor": accent_color,
                "discountedPrice": discounted_price,
                "fixedApy": fixed_apy,
                "currentPrice": current_price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.curreny_amount_entity import CurrenyAmountEntity

        d = dict(src_dict)
        market_address = d.pop("marketAddress")

        icon = d.pop("icon")

        token_symbol = d.pop("tokenSymbol")

        symbol = d.pop("symbol")

        accent_color = d.pop("accentColor")

        discounted_price = CurrenyAmountEntity.from_dict(d.pop("discountedPrice"))

        fixed_apy = d.pop("fixedApy")

        current_price = CurrenyAmountEntity.from_dict(d.pop("currentPrice"))

        featured_market_entity = cls(
            market_address=market_address,
            icon=icon,
            token_symbol=token_symbol,
            symbol=symbol,
            accent_color=accent_color,
            discounted_price=discounted_price,
            fixed_apy=fixed_apy,
            current_price=current_price,
        )

        featured_market_entity.additional_properties = d
        return featured_market_entity

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
