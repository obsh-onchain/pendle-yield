from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrenyAmountEntity")


@_attrs_define
class CurrenyAmountEntity:
    """
    Attributes:
        currency (str):
        amount (Union[None, Unset, float]):
    """

    currency: str
    amount: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        amount: Union[None, Unset, float]
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency")

        def _parse_amount(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        amount = _parse_amount(d.pop("amount", UNSET))

        curreny_amount_entity = cls(
            currency=currency,
            amount=amount,
        )

        curreny_amount_entity.additional_properties = d
        return curreny_amount_entity

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
