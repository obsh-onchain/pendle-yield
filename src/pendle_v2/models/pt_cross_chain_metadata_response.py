from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PtCrossChainMetadataResponse")


@_attrs_define
class PtCrossChainMetadataResponse:
    """
    Attributes:
        paired_tokens_out (list[str]): Array of token addresses that the PT can be swapped to
        amm_address (Union[Unset, str]): The address of the AMM
    """

    paired_tokens_out: list[str]
    amm_address: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        paired_tokens_out = self.paired_tokens_out

        amm_address = self.amm_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pairedTokensOut": paired_tokens_out,
            }
        )
        if amm_address is not UNSET:
            field_dict["ammAddress"] = amm_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        paired_tokens_out = cast(list[str], d.pop("pairedTokensOut"))

        amm_address = d.pop("ammAddress", UNSET)

        pt_cross_chain_metadata_response = cls(
            paired_tokens_out=paired_tokens_out,
            amm_address=amm_address,
        )

        pt_cross_chain_metadata_response.additional_properties = d
        return pt_cross_chain_metadata_response

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
