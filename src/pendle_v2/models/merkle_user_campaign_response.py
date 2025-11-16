import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="MerkleUserCampaignResponse")


@_attrs_define
class MerkleUserCampaignResponse:
    """
    Attributes:
        user (str):
        token (str):
        merkle_root (str):
        chain_id (float):
        asset_id (str):
        amount (str):
        to_timestamp (datetime.datetime):
        from_timestamp (datetime.datetime):
    """

    user: str
    token: str
    merkle_root: str
    chain_id: float
    asset_id: str
    amount: str
    to_timestamp: datetime.datetime
    from_timestamp: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user

        token = self.token

        merkle_root = self.merkle_root

        chain_id = self.chain_id

        asset_id = self.asset_id

        amount = self.amount

        to_timestamp = self.to_timestamp.isoformat()

        from_timestamp = self.from_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "token": token,
                "merkleRoot": merkle_root,
                "chainId": chain_id,
                "assetId": asset_id,
                "amount": amount,
                "toTimestamp": to_timestamp,
                "fromTimestamp": from_timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user = d.pop("user")

        token = d.pop("token")

        merkle_root = d.pop("merkleRoot")

        chain_id = d.pop("chainId")

        asset_id = d.pop("assetId")

        amount = d.pop("amount")

        to_timestamp = isoparse(d.pop("toTimestamp"))

        from_timestamp = isoparse(d.pop("fromTimestamp"))

        merkle_user_campaign_response = cls(
            user=user,
            token=token,
            merkle_root=merkle_root,
            chain_id=chain_id,
            asset_id=asset_id,
            amount=amount,
            to_timestamp=to_timestamp,
            from_timestamp=from_timestamp,
        )

        merkle_user_campaign_response.additional_properties = d
        return merkle_user_campaign_response

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
