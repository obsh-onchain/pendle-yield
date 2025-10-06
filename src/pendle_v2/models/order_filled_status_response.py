from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrderFilledStatusResponse")


@_attrs_define
class OrderFilledStatusResponse:
    """
    Attributes:
        net_input_from_maker (str): BigInt string of netInputFromMaker, the unit is the same as making amount
        net_output_to_maker (str): BigInt string of netOutputToMaker, the unit is SY if the order is PT_FOR_TOKEN or
            YT_FOR_TOKEN, otherwise, the unit it PT or YT depends on type of order
        fee_amount (str): BigInt string of feeAmount, in SY
        notional_volume (str): BigInt string of notionalVolume, in SY
    """

    net_input_from_maker: str
    net_output_to_maker: str
    fee_amount: str
    notional_volume: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        net_input_from_maker = self.net_input_from_maker

        net_output_to_maker = self.net_output_to_maker

        fee_amount = self.fee_amount

        notional_volume = self.notional_volume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "netInputFromMaker": net_input_from_maker,
                "netOutputToMaker": net_output_to_maker,
                "feeAmount": fee_amount,
                "notionalVolume": notional_volume,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        net_input_from_maker = d.pop("netInputFromMaker")

        net_output_to_maker = d.pop("netOutputToMaker")

        fee_amount = d.pop("feeAmount")

        notional_volume = d.pop("notionalVolume")

        order_filled_status_response = cls(
            net_input_from_maker=net_input_from_maker,
            net_output_to_maker=net_output_to_maker,
            fee_amount=fee_amount,
            notional_volume=notional_volume,
        )

        order_filled_status_response.additional_properties = d
        return order_filled_status_response

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
