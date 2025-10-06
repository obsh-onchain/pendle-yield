import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.market_position import MarketPosition
    from ..models.sy_position import SyPosition


T = TypeVar("T", bound="UserPositionsResponse")


@_attrs_define
class UserPositionsResponse:
    """
    Attributes:
        chain_id (float): Chain ID Example: 1.
        total_open (float): Total number of open positions Example: 100.
        total_closed (float): Total number of closed positions Example: 100.
        total_sy (float): Total number of SY positions Example: 100.
        open_positions (list['MarketPosition']): Array of user token positions
        closed_positions (list['MarketPosition']): Array of closed user token positions
        sy_positions (list['SyPosition']): Array of user SY positions
        updated_at (datetime.datetime): Date time of the last update Example: 2021-01-01T00:00:00.000Z.
        error_message (Union[Unset, str]): Error message when there is something wrong Example: Error message.
    """

    chain_id: float
    total_open: float
    total_closed: float
    total_sy: float
    open_positions: list["MarketPosition"]
    closed_positions: list["MarketPosition"]
    sy_positions: list["SyPosition"]
    updated_at: datetime.datetime
    error_message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chain_id = self.chain_id

        total_open = self.total_open

        total_closed = self.total_closed

        total_sy = self.total_sy

        open_positions = []
        for open_positions_item_data in self.open_positions:
            open_positions_item = open_positions_item_data.to_dict()
            open_positions.append(open_positions_item)

        closed_positions = []
        for closed_positions_item_data in self.closed_positions:
            closed_positions_item = closed_positions_item_data.to_dict()
            closed_positions.append(closed_positions_item)

        sy_positions = []
        for sy_positions_item_data in self.sy_positions:
            sy_positions_item = sy_positions_item_data.to_dict()
            sy_positions.append(sy_positions_item)

        updated_at = self.updated_at.isoformat()

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chainId": chain_id,
                "totalOpen": total_open,
                "totalClosed": total_closed,
                "totalSy": total_sy,
                "openPositions": open_positions,
                "closedPositions": closed_positions,
                "syPositions": sy_positions,
                "updatedAt": updated_at,
            }
        )
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market_position import MarketPosition
        from ..models.sy_position import SyPosition

        d = dict(src_dict)
        chain_id = d.pop("chainId")

        total_open = d.pop("totalOpen")

        total_closed = d.pop("totalClosed")

        total_sy = d.pop("totalSy")

        open_positions = []
        _open_positions = d.pop("openPositions")
        for open_positions_item_data in _open_positions:
            open_positions_item = MarketPosition.from_dict(open_positions_item_data)

            open_positions.append(open_positions_item)

        closed_positions = []
        _closed_positions = d.pop("closedPositions")
        for closed_positions_item_data in _closed_positions:
            closed_positions_item = MarketPosition.from_dict(closed_positions_item_data)

            closed_positions.append(closed_positions_item)

        sy_positions = []
        _sy_positions = d.pop("syPositions")
        for sy_positions_item_data in _sy_positions:
            sy_positions_item = SyPosition.from_dict(sy_positions_item_data)

            sy_positions.append(sy_positions_item)

        updated_at = isoparse(d.pop("updatedAt"))

        error_message = d.pop("errorMessage", UNSET)

        user_positions_response = cls(
            chain_id=chain_id,
            total_open=total_open,
            total_closed=total_closed,
            total_sy=total_sy,
            open_positions=open_positions,
            closed_positions=closed_positions,
            sy_positions=sy_positions,
            updated_at=updated_at,
            error_message=error_message,
        )

        user_positions_response.additional_properties = d
        return user_positions_response

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
