from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cross_chain_pt_data import CrossChainPtData


T = TypeVar("T", bound="ChainIdSimplifiedData")


@_attrs_define
class ChainIdSimplifiedData:
    """
    Attributes:
        chain_id (float):
        sys (list[str]): list of SY addresses
        markets (list[str]): list of market addresses
        pts (list[str]): list of PT addresses
        yts (list[str]): list of YT addresses
        cross_pts (list['CrossChainPtData']): list of cross chain pt data
    """

    chain_id: float
    sys: list[str]
    markets: list[str]
    pts: list[str]
    yts: list[str]
    cross_pts: list["CrossChainPtData"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chain_id = self.chain_id

        sys = self.sys

        markets = self.markets

        pts = self.pts

        yts = self.yts

        cross_pts = []
        for cross_pts_item_data in self.cross_pts:
            cross_pts_item = cross_pts_item_data.to_dict()
            cross_pts.append(cross_pts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chainId": chain_id,
                "sys": sys,
                "markets": markets,
                "pts": pts,
                "yts": yts,
                "crossPts": cross_pts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cross_chain_pt_data import CrossChainPtData

        d = dict(src_dict)
        chain_id = d.pop("chainId")

        sys = cast(list[str], d.pop("sys"))

        markets = cast(list[str], d.pop("markets"))

        pts = cast(list[str], d.pop("pts"))

        yts = cast(list[str], d.pop("yts"))

        cross_pts = []
        _cross_pts = d.pop("crossPts")
        for cross_pts_item_data in _cross_pts:
            cross_pts_item = CrossChainPtData.from_dict(cross_pts_item_data)

            cross_pts.append(cross_pts_item)

        chain_id_simplified_data = cls(
            chain_id=chain_id,
            sys=sys,
            markets=markets,
            pts=pts,
            yts=yts,
            cross_pts=cross_pts,
        )

        chain_id_simplified_data.additional_properties = d
        return chain_id_simplified_data

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
