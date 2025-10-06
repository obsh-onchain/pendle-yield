from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_positions_response import UserPositionsResponse


T = TypeVar("T", bound="UserPositionsCrossChainResponse")


@_attrs_define
class UserPositionsCrossChainResponse:
    """
    Attributes:
        positions (list['UserPositionsResponse']): Array of user positions
    """

    positions: list["UserPositionsResponse"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        positions = []
        for positions_item_data in self.positions:
            positions_item = positions_item_data.to_dict()
            positions.append(positions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "positions": positions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_positions_response import UserPositionsResponse

        d = dict(src_dict)
        positions = []
        _positions = d.pop("positions")
        for positions_item_data in _positions:
            positions_item = UserPositionsResponse.from_dict(positions_item_data)

            positions.append(positions_item)

        user_positions_cross_chain_response = cls(
            positions=positions,
        )

        user_positions_cross_chain_response.additional_properties = d
        return user_positions_cross_chain_response

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
