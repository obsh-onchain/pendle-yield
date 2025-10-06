from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PtYtImpliedYieldChangeAmountResponse")


@_attrs_define
class PtYtImpliedYieldChangeAmountResponse:
    """
    Attributes:
        pt_movement_up_usd (Union[Unset, float]):
        pt_movement_down_usd (Union[Unset, float]):
        yt_movement_up_usd (Union[Unset, float]):
        yt_movement_down_usd (Union[Unset, float]):
    """

    pt_movement_up_usd: Union[Unset, float] = UNSET
    pt_movement_down_usd: Union[Unset, float] = UNSET
    yt_movement_up_usd: Union[Unset, float] = UNSET
    yt_movement_down_usd: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pt_movement_up_usd = self.pt_movement_up_usd

        pt_movement_down_usd = self.pt_movement_down_usd

        yt_movement_up_usd = self.yt_movement_up_usd

        yt_movement_down_usd = self.yt_movement_down_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pt_movement_up_usd is not UNSET:
            field_dict["ptMovementUpUsd"] = pt_movement_up_usd
        if pt_movement_down_usd is not UNSET:
            field_dict["ptMovementDownUsd"] = pt_movement_down_usd
        if yt_movement_up_usd is not UNSET:
            field_dict["ytMovementUpUsd"] = yt_movement_up_usd
        if yt_movement_down_usd is not UNSET:
            field_dict["ytMovementDownUsd"] = yt_movement_down_usd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pt_movement_up_usd = d.pop("ptMovementUpUsd", UNSET)

        pt_movement_down_usd = d.pop("ptMovementDownUsd", UNSET)

        yt_movement_up_usd = d.pop("ytMovementUpUsd", UNSET)

        yt_movement_down_usd = d.pop("ytMovementDownUsd", UNSET)

        pt_yt_implied_yield_change_amount_response = cls(
            pt_movement_up_usd=pt_movement_up_usd,
            pt_movement_down_usd=pt_movement_down_usd,
            yt_movement_up_usd=yt_movement_up_usd,
            yt_movement_down_usd=yt_movement_down_usd,
        )

        pt_yt_implied_yield_change_amount_response.additional_properties = d
        return pt_yt_implied_yield_change_amount_response

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
