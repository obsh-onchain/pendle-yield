from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.position import Position


T = TypeVar("T", bound="MarketPosition")


@_attrs_define
class MarketPosition:
    """
    Attributes:
        market_id (str): Unique identifier of the market Example: 1-0xabc....
        pt (Position):
        yt (Position):
        lp (Position):
    """

    market_id: str
    pt: "Position"
    yt: "Position"
    lp: "Position"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        market_id = self.market_id

        pt = self.pt.to_dict()

        yt = self.yt.to_dict()

        lp = self.lp.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "marketId": market_id,
                "pt": pt,
                "yt": yt,
                "lp": lp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.position import Position

        d = dict(src_dict)
        market_id = d.pop("marketId")

        pt = Position.from_dict(d.pop("pt"))

        yt = Position.from_dict(d.pop("yt"))

        lp = Position.from_dict(d.pop("lp"))

        market_position = cls(
            market_id=market_id,
            pt=pt,
            yt=yt,
            lp=lp,
        )

        market_position.additional_properties = d
        return market_position

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
