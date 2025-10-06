from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrderStateResponse")


@_attrs_define
class OrderStateResponse:
    """
    Attributes:
        order_type (str):
        exchange_rate (str):
        ps_amount_to_taker (str):
        ps_amount_from_taker (str):
        ys_amount_to_taker (str):
        ys_amount_from_taker (str):
        fee (str):
        ps_rate (float):
        ys_rate (float):
        net_to_maker_if_fully_filled (str): In SY if the order is PY for token
        net_from_maker_if_fully_filled (str): The difference with currentMakingAmount is that this is in SY if
            currentMakingAmount in tokenIn
        notional_volume (str):
        matchable_amount (str):
        notional_volume_usd (float):
    """

    order_type: str
    exchange_rate: str
    ps_amount_to_taker: str
    ps_amount_from_taker: str
    ys_amount_to_taker: str
    ys_amount_from_taker: str
    fee: str
    ps_rate: float
    ys_rate: float
    net_to_maker_if_fully_filled: str
    net_from_maker_if_fully_filled: str
    notional_volume: str
    matchable_amount: str
    notional_volume_usd: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_type = self.order_type

        exchange_rate = self.exchange_rate

        ps_amount_to_taker = self.ps_amount_to_taker

        ps_amount_from_taker = self.ps_amount_from_taker

        ys_amount_to_taker = self.ys_amount_to_taker

        ys_amount_from_taker = self.ys_amount_from_taker

        fee = self.fee

        ps_rate = self.ps_rate

        ys_rate = self.ys_rate

        net_to_maker_if_fully_filled = self.net_to_maker_if_fully_filled

        net_from_maker_if_fully_filled = self.net_from_maker_if_fully_filled

        notional_volume = self.notional_volume

        matchable_amount = self.matchable_amount

        notional_volume_usd = self.notional_volume_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderType": order_type,
                "exchangeRate": exchange_rate,
                "psAmountToTaker": ps_amount_to_taker,
                "psAmountFromTaker": ps_amount_from_taker,
                "ysAmountToTaker": ys_amount_to_taker,
                "ysAmountFromTaker": ys_amount_from_taker,
                "fee": fee,
                "psRate": ps_rate,
                "ysRate": ys_rate,
                "netToMakerIfFullyFilled": net_to_maker_if_fully_filled,
                "netFromMakerIfFullyFilled": net_from_maker_if_fully_filled,
                "notionalVolume": notional_volume,
                "matchableAmount": matchable_amount,
                "notionalVolumeUSD": notional_volume_usd,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_type = d.pop("orderType")

        exchange_rate = d.pop("exchangeRate")

        ps_amount_to_taker = d.pop("psAmountToTaker")

        ps_amount_from_taker = d.pop("psAmountFromTaker")

        ys_amount_to_taker = d.pop("ysAmountToTaker")

        ys_amount_from_taker = d.pop("ysAmountFromTaker")

        fee = d.pop("fee")

        ps_rate = d.pop("psRate")

        ys_rate = d.pop("ysRate")

        net_to_maker_if_fully_filled = d.pop("netToMakerIfFullyFilled")

        net_from_maker_if_fully_filled = d.pop("netFromMakerIfFullyFilled")

        notional_volume = d.pop("notionalVolume")

        matchable_amount = d.pop("matchableAmount")

        notional_volume_usd = d.pop("notionalVolumeUSD")

        order_state_response = cls(
            order_type=order_type,
            exchange_rate=exchange_rate,
            ps_amount_to_taker=ps_amount_to_taker,
            ps_amount_from_taker=ps_amount_from_taker,
            ys_amount_to_taker=ys_amount_to_taker,
            ys_amount_from_taker=ys_amount_from_taker,
            fee=fee,
            ps_rate=ps_rate,
            ys_rate=ys_rate,
            net_to_maker_if_fully_filled=net_to_maker_if_fully_filled,
            net_from_maker_if_fully_filled=net_from_maker_if_fully_filled,
            notional_volume=notional_volume,
            matchable_amount=matchable_amount,
            notional_volume_usd=notional_volume_usd,
        )

        order_state_response.additional_properties = d
        return order_state_response

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
