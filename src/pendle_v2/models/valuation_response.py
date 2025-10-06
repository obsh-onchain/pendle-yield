from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValuationResponse")


@_attrs_define
class ValuationResponse:
    """
    Attributes:
        usd (Union[None, Unset, float]):
        acc (Union[None, Unset, float]):
    """

    usd: Union[None, Unset, float] = UNSET
    acc: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        usd: Union[None, Unset, float]
        if isinstance(self.usd, Unset):
            usd = UNSET
        else:
            usd = self.usd

        acc: Union[None, Unset, float]
        if isinstance(self.acc, Unset):
            acc = UNSET
        else:
            acc = self.acc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if usd is not UNSET:
            field_dict["usd"] = usd
        if acc is not UNSET:
            field_dict["acc"] = acc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_usd(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        usd = _parse_usd(d.pop("usd", UNSET))

        def _parse_acc(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        acc = _parse_acc(d.pop("acc", UNSET))

        valuation_response = cls(
            usd=usd,
            acc=acc,
        )

        valuation_response.additional_properties = d
        return valuation_response

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
