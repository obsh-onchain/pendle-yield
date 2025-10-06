import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MerkleProofResponse")


@_attrs_define
class MerkleProofResponse:
    """
    Attributes:
        proof (list[str]):
        accrued_amount (str):
        updated_at (datetime.datetime):
        merkle_root (str): Merkle root hash of the merkle tree
        verify_call_data (Union[Unset, str]): Calldata to verify the proof
    """

    proof: list[str]
    accrued_amount: str
    updated_at: datetime.datetime
    merkle_root: str
    verify_call_data: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proof = self.proof

        accrued_amount = self.accrued_amount

        updated_at = self.updated_at.isoformat()

        merkle_root = self.merkle_root

        verify_call_data = self.verify_call_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proof": proof,
                "accruedAmount": accrued_amount,
                "updatedAt": updated_at,
                "merkleRoot": merkle_root,
            }
        )
        if verify_call_data is not UNSET:
            field_dict["verifyCallData"] = verify_call_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        proof = cast(list[str], d.pop("proof"))

        accrued_amount = d.pop("accruedAmount")

        updated_at = isoparse(d.pop("updatedAt"))

        merkle_root = d.pop("merkleRoot")

        verify_call_data = d.pop("verifyCallData", UNSET)

        merkle_proof_response = cls(
            proof=proof,
            accrued_amount=accrued_amount,
            updated_at=updated_at,
            merkle_root=merkle_root,
            verify_call_data=verify_call_data,
        )

        merkle_proof_response.additional_properties = d
        return merkle_proof_response

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
