import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="VoteData")


@_attrs_define
class VoteData:
    """
    Attributes:
        tx_hash (str):
        timestamp (datetime.datetime):
        pool_chain_id (float):
        pool_address (str):
        user (str):
        weight (float):
        ve_pendle_vote (float):
    """

    tx_hash: str
    timestamp: datetime.datetime
    pool_chain_id: float
    pool_address: str
    user: str
    weight: float
    ve_pendle_vote: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tx_hash = self.tx_hash

        timestamp = self.timestamp.isoformat()

        pool_chain_id = self.pool_chain_id

        pool_address = self.pool_address

        user = self.user

        weight = self.weight

        ve_pendle_vote = self.ve_pendle_vote

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "txHash": tx_hash,
                "timestamp": timestamp,
                "poolChainId": pool_chain_id,
                "poolAddress": pool_address,
                "user": user,
                "weight": weight,
                "vePendleVote": ve_pendle_vote,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tx_hash = d.pop("txHash")

        timestamp = isoparse(d.pop("timestamp"))

        pool_chain_id = d.pop("poolChainId")

        pool_address = d.pop("poolAddress")

        user = d.pop("user")

        weight = d.pop("weight")

        ve_pendle_vote = d.pop("vePendleVote")

        vote_data = cls(
            tx_hash=tx_hash,
            timestamp=timestamp,
            pool_chain_id=pool_chain_id,
            pool_address=pool_address,
            user=user,
            weight=weight,
            ve_pendle_vote=ve_pendle_vote,
        )

        vote_data.additional_properties = d
        return vote_data

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
