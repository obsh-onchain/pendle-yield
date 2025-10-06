from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sy_token_out_route_response import SyTokenOutRouteResponse


T = TypeVar("T", bound="SyTokenOutRouteListResponse")


@_attrs_define
class SyTokenOutRouteListResponse:
    """
    Attributes:
        token_out_routes (list['SyTokenOutRouteResponse']):
    """

    token_out_routes: list["SyTokenOutRouteResponse"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token_out_routes = []
        for token_out_routes_item_data in self.token_out_routes:
            token_out_routes_item = token_out_routes_item_data.to_dict()
            token_out_routes.append(token_out_routes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tokenOutRoutes": token_out_routes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sy_token_out_route_response import SyTokenOutRouteResponse

        d = dict(src_dict)
        token_out_routes = []
        _token_out_routes = d.pop("tokenOutRoutes")
        for token_out_routes_item_data in _token_out_routes:
            token_out_routes_item = SyTokenOutRouteResponse.from_dict(token_out_routes_item_data)

            token_out_routes.append(token_out_routes_item)

        sy_token_out_route_list_response = cls(
            token_out_routes=token_out_routes,
        )

        sy_token_out_route_list_response.additional_properties = d
        return sy_token_out_route_list_response

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
