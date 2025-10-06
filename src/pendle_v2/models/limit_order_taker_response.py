from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.limit_order_response import LimitOrderResponse


T = TypeVar("T", bound="LimitOrderTakerResponse")


@_attrs_define
class LimitOrderTakerResponse:
    """
    Attributes:
        order (LimitOrderResponse):
        making_amount (str): Amount to be used to fill the order, the unit is the same as the unit of limit order'
            making amount
        net_from_taker (str): Amount from taker need to fully fill this order, the unit is SY if the market order is
            TOKEN_FOR_PT or TOKEN_FOR_YT, otherwise, the unit it PT or YT depends on type of order
        net_to_taker (str): Actual making amount to taker, the unit is SY if the market order is PT_FOR_TOKEN or
            YT_FOR_TOKEN, otherwise, the unit it PT or YT depends on type of order
    """

    order: "LimitOrderResponse"
    making_amount: str
    net_from_taker: str
    net_to_taker: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order = self.order.to_dict()

        making_amount = self.making_amount

        net_from_taker = self.net_from_taker

        net_to_taker = self.net_to_taker

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order": order,
                "makingAmount": making_amount,
                "netFromTaker": net_from_taker,
                "netToTaker": net_to_taker,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.limit_order_response import LimitOrderResponse

        d = dict(src_dict)
        order = LimitOrderResponse.from_dict(d.pop("order"))

        making_amount = d.pop("makingAmount")

        net_from_taker = d.pop("netFromTaker")

        net_to_taker = d.pop("netToTaker")

        limit_order_taker_response = cls(
            order=order,
            making_amount=making_amount,
            net_from_taker=net_from_taker,
            net_to_taker=net_to_taker,
        )

        limit_order_taker_response.additional_properties = d
        return limit_order_taker_response

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
