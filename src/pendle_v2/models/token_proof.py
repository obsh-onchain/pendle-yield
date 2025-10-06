from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenProof")


@_attrs_define
class TokenProof:
    """
    Attributes:
        token (str):
        proof (list[str]):
        accrued_amount (str):
        verify_call_data (Union[Unset, str]): Calldata to verify the proof
    """

    token: str
    proof: list[str]
    accrued_amount: str
    verify_call_data: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        proof = self.proof

        accrued_amount = self.accrued_amount

        verify_call_data = self.verify_call_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "proof": proof,
                "accruedAmount": accrued_amount,
            }
        )
        if verify_call_data is not UNSET:
            field_dict["verifyCallData"] = verify_call_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        proof = cast(list[str], d.pop("proof"))

        accrued_amount = d.pop("accruedAmount")

        verify_call_data = d.pop("verifyCallData", UNSET)

        token_proof = cls(
            token=token,
            proof=proof,
            accrued_amount=accrued_amount,
            verify_call_data=verify_call_data,
        )

        token_proof.additional_properties = d
        return token_proof

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
