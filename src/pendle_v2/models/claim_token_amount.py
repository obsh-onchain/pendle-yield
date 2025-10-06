from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ClaimTokenAmount")


@_attrs_define
class ClaimTokenAmount:
    """
    Attributes:
        token (str): Token id Example: 1-0x123....
        amount (str): Amount of tokens Example: 1000000000000000000.
    """

    token: str
    amount: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        amount = d.pop("amount")

        claim_token_amount = cls(
            token=token,
            amount=amount,
        )

        claim_token_amount.additional_properties = d
        return claim_token_amount

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
