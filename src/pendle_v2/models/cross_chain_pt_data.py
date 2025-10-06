from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CrossChainPtData")


@_attrs_define
class CrossChainPtData:
    """
    Attributes:
        spoke_pt (str): spoke pt address
        hub_pt (str): hub pt address
        hub_chain_id (float): hub chain id
    """

    spoke_pt: str
    hub_pt: str
    hub_chain_id: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spoke_pt = self.spoke_pt

        hub_pt = self.hub_pt

        hub_chain_id = self.hub_chain_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spokePt": spoke_pt,
                "hubPt": hub_pt,
                "hubChainId": hub_chain_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        spoke_pt = d.pop("spokePt")

        hub_pt = d.pop("hubPt")

        hub_chain_id = d.pop("hubChainId")

        cross_chain_pt_data = cls(
            spoke_pt=spoke_pt,
            hub_pt=hub_pt,
            hub_chain_id=hub_chain_id,
        )

        cross_chain_pt_data.additional_properties = d
        return cross_chain_pt_data

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
