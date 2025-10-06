from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SpokePtData")


@_attrs_define
class SpokePtData:
    """
    Attributes:
        spoke_chain_id (float): Spoke PT chain ID Example: 1.
        spoke_address (str): Spoke PT address Example: 0x1234567890123456789012345678901234567890.
    """

    spoke_chain_id: float
    spoke_address: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spoke_chain_id = self.spoke_chain_id

        spoke_address = self.spoke_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spokeChainId": spoke_chain_id,
                "spokeAddress": spoke_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        spoke_chain_id = d.pop("spokeChainId")

        spoke_address = d.pop("spokeAddress")

        spoke_pt_data = cls(
            spoke_chain_id=spoke_chain_id,
            spoke_address=spoke_address,
        )

        spoke_pt_data.additional_properties = d
        return spoke_pt_data

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
