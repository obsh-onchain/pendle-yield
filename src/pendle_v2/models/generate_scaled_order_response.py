from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.generate_limit_order_data_response import GenerateLimitOrderDataResponse


T = TypeVar("T", bound="GenerateScaledOrderResponse")


@_attrs_define
class GenerateScaledOrderResponse:
    """
    Attributes:
        orders (list['GenerateLimitOrderDataResponse']): List of generated limit orders
    """

    orders: list["GenerateLimitOrderDataResponse"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        orders = []
        for orders_item_data in self.orders:
            orders_item = orders_item_data.to_dict()
            orders.append(orders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orders": orders,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_limit_order_data_response import GenerateLimitOrderDataResponse

        d = dict(src_dict)
        orders = []
        _orders = d.pop("orders")
        for orders_item_data in _orders:
            orders_item = GenerateLimitOrderDataResponse.from_dict(orders_item_data)

            orders.append(orders_item)

        generate_scaled_order_response = cls(
            orders=orders,
        )

        generate_scaled_order_response.additional_properties = d
        return generate_scaled_order_response

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
