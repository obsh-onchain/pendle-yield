from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SwapPtCrossChainData")


@_attrs_define
class SwapPtCrossChainData:
    """
    Attributes:
        net_token_out (str): Net token output amount
        net_pt_in (str): Net PT input amount
    """

    net_token_out: str
    net_pt_in: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        net_token_out = self.net_token_out

        net_pt_in = self.net_pt_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "netTokenOut": net_token_out,
                "netPtIn": net_pt_in,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        net_token_out = d.pop("netTokenOut")

        net_pt_in = d.pop("netPtIn")

        swap_pt_cross_chain_data = cls(
            net_token_out=net_token_out,
            net_pt_in=net_pt_in,
        )

        swap_pt_cross_chain_data.additional_properties = d
        return swap_pt_cross_chain_data

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
