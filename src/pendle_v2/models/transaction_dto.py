from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TransactionDto")


@_attrs_define
class TransactionDto:
    """
    Attributes:
        data (str): Transaction data
        to (str): Transaction receiver
        from_ (str): Transaction sender
        value (str): Transaction value
    """

    data: str
    to: str
    from_: str
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        to = self.to

        from_ = self.from_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "to": to,
                "from": from_,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = d.pop("data")

        to = d.pop("to")

        from_ = d.pop("from")

        value = d.pop("value")

        transaction_dto = cls(
            data=data,
            to=to,
            from_=from_,
            value=value,
        )

        transaction_dto.additional_properties = d
        return transaction_dto

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
