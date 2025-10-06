import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.token_proof import TokenProof


T = TypeVar("T", bound="MultiTokenMerkleProofResponse")


@_attrs_define
class MultiTokenMerkleProofResponse:
    """
    Attributes:
        proof (list['TokenProof']):
        merkle_root (str):
        updated_at (datetime.datetime):
        chain_id (float):
        distributor_address (str):
        campaign_id (str):
    """

    proof: list["TokenProof"]
    merkle_root: str
    updated_at: datetime.datetime
    chain_id: float
    distributor_address: str
    campaign_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proof = []
        for proof_item_data in self.proof:
            proof_item = proof_item_data.to_dict()
            proof.append(proof_item)

        merkle_root = self.merkle_root

        updated_at = self.updated_at.isoformat()

        chain_id = self.chain_id

        distributor_address = self.distributor_address

        campaign_id = self.campaign_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proof": proof,
                "merkleRoot": merkle_root,
                "updatedAt": updated_at,
                "chainId": chain_id,
                "distributorAddress": distributor_address,
                "campaignId": campaign_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_proof import TokenProof

        d = dict(src_dict)
        proof = []
        _proof = d.pop("proof")
        for proof_item_data in _proof:
            proof_item = TokenProof.from_dict(proof_item_data)

            proof.append(proof_item)

        merkle_root = d.pop("merkleRoot")

        updated_at = isoparse(d.pop("updatedAt"))

        chain_id = d.pop("chainId")

        distributor_address = d.pop("distributorAddress")

        campaign_id = d.pop("campaignId")

        multi_token_merkle_proof_response = cls(
            proof=proof,
            merkle_root=merkle_root,
            updated_at=updated_at,
            chain_id=chain_id,
            distributor_address=distributor_address,
            campaign_id=campaign_id,
        )

        multi_token_merkle_proof_response.additional_properties = d
        return multi_token_merkle_proof_response

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
