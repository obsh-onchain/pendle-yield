from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pool_response import PoolResponse


T = TypeVar("T", bound="VoteResponse")


@_attrs_define
class VoteResponse:
    """
    Attributes:
        pool (PoolResponse):
        votes (float):
        percentage (float):
    """

    pool: "PoolResponse"
    votes: float
    percentage: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pool = self.pool.to_dict()

        votes = self.votes

        percentage = self.percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pool": pool,
                "votes": votes,
                "percentage": percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pool_response import PoolResponse

        d = dict(src_dict)
        pool = PoolResponse.from_dict(d.pop("pool"))

        votes = d.pop("votes")

        percentage = d.pop("percentage")

        vote_response = cls(
            pool=pool,
            votes=votes,
            percentage=percentage,
        )

        vote_response.additional_properties = d
        return vote_response

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
