from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.spoke_pt_data import SpokePtData


T = TypeVar("T", bound="PtCrossChainData")


@_attrs_define
class PtCrossChainData:
    """
    Attributes:
        hub_pt_chain_id (float): Hub PT chain ID
        hub_pt_address (str): Hub PT address
        spoke_pts (list['SpokePtData']): Spoke PTs
    """

    hub_pt_chain_id: float
    hub_pt_address: str
    spoke_pts: list["SpokePtData"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hub_pt_chain_id = self.hub_pt_chain_id

        hub_pt_address = self.hub_pt_address

        spoke_pts = []
        for spoke_pts_item_data in self.spoke_pts:
            spoke_pts_item = spoke_pts_item_data.to_dict()
            spoke_pts.append(spoke_pts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hubPtChainId": hub_pt_chain_id,
                "hubPtAddress": hub_pt_address,
                "spokePts": spoke_pts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spoke_pt_data import SpokePtData

        d = dict(src_dict)
        hub_pt_chain_id = d.pop("hubPtChainId")

        hub_pt_address = d.pop("hubPtAddress")

        spoke_pts = []
        _spoke_pts = d.pop("spokePts")
        for spoke_pts_item_data in _spoke_pts:
            spoke_pts_item = SpokePtData.from_dict(spoke_pts_item_data)

            spoke_pts.append(spoke_pts_item)

        pt_cross_chain_data = cls(
            hub_pt_chain_id=hub_pt_chain_id,
            hub_pt_address=hub_pt_address,
            spoke_pts=spoke_pts,
        )

        pt_cross_chain_data.additional_properties = d
        return pt_cross_chain_data

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
