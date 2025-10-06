from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MarketTokensResponse")


@_attrs_define
class MarketTokensResponse:
    """
    Attributes:
        tokens_mint_sy (list[str]): tokens can be use for tokenMintSy
        tokens_redeem_sy (list[str]): tokens can be use for tokenRedeemSy
        tokens_in (list[str]): input tokens of swap or zap function
        tokens_out (list[str]): output tokens of swap or zap function
    """

    tokens_mint_sy: list[str]
    tokens_redeem_sy: list[str]
    tokens_in: list[str]
    tokens_out: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tokens_mint_sy = self.tokens_mint_sy

        tokens_redeem_sy = self.tokens_redeem_sy

        tokens_in = self.tokens_in

        tokens_out = self.tokens_out

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tokensMintSy": tokens_mint_sy,
                "tokensRedeemSy": tokens_redeem_sy,
                "tokensIn": tokens_in,
                "tokensOut": tokens_out,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tokens_mint_sy = cast(list[str], d.pop("tokensMintSy"))

        tokens_redeem_sy = cast(list[str], d.pop("tokensRedeemSy"))

        tokens_in = cast(list[str], d.pop("tokensIn"))

        tokens_out = cast(list[str], d.pop("tokensOut"))

        market_tokens_response = cls(
            tokens_mint_sy=tokens_mint_sy,
            tokens_redeem_sy=tokens_redeem_sy,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
        )

        market_tokens_response.additional_properties = d
        return market_tokens_response

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
