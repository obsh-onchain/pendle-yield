from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MakerResponse")


@_attrs_define
class MakerResponse:
    """
    Attributes:
        maker (str):
        sum_order_size_usd (float):
        num_orders (float):
    """

    maker: str
    sum_order_size_usd: float
    num_orders: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        maker = self.maker

        sum_order_size_usd = self.sum_order_size_usd

        num_orders = self.num_orders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maker": maker,
                "sumOrderSizeUsd": sum_order_size_usd,
                "numOrders": num_orders,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        maker = d.pop("maker")

        sum_order_size_usd = d.pop("sumOrderSizeUsd")

        num_orders = d.pop("numOrders")

        maker_response = cls(
            maker=maker,
            sum_order_size_usd=sum_order_size_usd,
            num_orders=num_orders,
        )

        maker_response.additional_properties = d
        return maker_response

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
