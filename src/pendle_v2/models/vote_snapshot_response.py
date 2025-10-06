import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.vote_response import VoteResponse


T = TypeVar("T", bound="VoteSnapshotResponse")


@_attrs_define
class VoteSnapshotResponse:
    """
    Attributes:
        votes (list['VoteResponse']):
        total_pools (float):
        total_votes (float):
        epoch (datetime.datetime):
    """

    votes: list["VoteResponse"]
    total_pools: float
    total_votes: float
    epoch: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        votes = []
        for votes_item_data in self.votes:
            votes_item = votes_item_data.to_dict()
            votes.append(votes_item)

        total_pools = self.total_pools

        total_votes = self.total_votes

        epoch = self.epoch.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "votes": votes,
                "totalPools": total_pools,
                "totalVotes": total_votes,
                "epoch": epoch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vote_response import VoteResponse

        d = dict(src_dict)
        votes = []
        _votes = d.pop("votes")
        for votes_item_data in _votes:
            votes_item = VoteResponse.from_dict(votes_item_data)

            votes.append(votes_item)

        total_pools = d.pop("totalPools")

        total_votes = d.pop("totalVotes")

        epoch = isoparse(d.pop("epoch"))

        vote_snapshot_response = cls(
            votes=votes,
            total_pools=total_pools,
            total_votes=total_votes,
            epoch=epoch,
        )

        vote_snapshot_response.additional_properties = d
        return vote_snapshot_response

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
