from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vote_v2_response import VoteV2Response


T = TypeVar("T", bound="PoolV2Response")


@_attrs_define
class PoolV2Response:
    """
    Attributes:
        id (str):
        symbol (str):
        expiry (str):
        current_voter_apr (Union[Unset, float]):
        last_epoch_voter_apr (Union[Unset, float]):
        current_swap_fee (Union[Unset, float]):
        last_epoch_swap_fee (Union[Unset, float]):
        projected_voter_apr (Union[Unset, float]):
        projected_votes (Union['VoteV2Response', None, Unset]):
        current_votes (Union['VoteV2Response', None, Unset]):
        expected_cap (Union[Unset, str]):
        current_cap (Union[Unset, str]):
    """

    id: str
    symbol: str
    expiry: str
    current_voter_apr: Union[Unset, float] = UNSET
    last_epoch_voter_apr: Union[Unset, float] = UNSET
    current_swap_fee: Union[Unset, float] = UNSET
    last_epoch_swap_fee: Union[Unset, float] = UNSET
    projected_voter_apr: Union[Unset, float] = UNSET
    projected_votes: Union["VoteV2Response", None, Unset] = UNSET
    current_votes: Union["VoteV2Response", None, Unset] = UNSET
    expected_cap: Union[Unset, str] = UNSET
    current_cap: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.vote_v2_response import VoteV2Response

        id = self.id

        symbol = self.symbol

        expiry = self.expiry

        current_voter_apr = self.current_voter_apr

        last_epoch_voter_apr = self.last_epoch_voter_apr

        current_swap_fee = self.current_swap_fee

        last_epoch_swap_fee = self.last_epoch_swap_fee

        projected_voter_apr = self.projected_voter_apr

        projected_votes: Union[None, Unset, dict[str, Any]]
        if isinstance(self.projected_votes, Unset):
            projected_votes = UNSET
        elif isinstance(self.projected_votes, VoteV2Response):
            projected_votes = self.projected_votes.to_dict()
        else:
            projected_votes = self.projected_votes

        current_votes: Union[None, Unset, dict[str, Any]]
        if isinstance(self.current_votes, Unset):
            current_votes = UNSET
        elif isinstance(self.current_votes, VoteV2Response):
            current_votes = self.current_votes.to_dict()
        else:
            current_votes = self.current_votes

        expected_cap = self.expected_cap

        current_cap = self.current_cap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "symbol": symbol,
                "expiry": expiry,
            }
        )
        if current_voter_apr is not UNSET:
            field_dict["currentVoterApr"] = current_voter_apr
        if last_epoch_voter_apr is not UNSET:
            field_dict["lastEpochVoterApr"] = last_epoch_voter_apr
        if current_swap_fee is not UNSET:
            field_dict["currentSwapFee"] = current_swap_fee
        if last_epoch_swap_fee is not UNSET:
            field_dict["lastEpochSwapFee"] = last_epoch_swap_fee
        if projected_voter_apr is not UNSET:
            field_dict["projectedVoterApr"] = projected_voter_apr
        if projected_votes is not UNSET:
            field_dict["projectedVotes"] = projected_votes
        if current_votes is not UNSET:
            field_dict["currentVotes"] = current_votes
        if expected_cap is not UNSET:
            field_dict["expectedCap"] = expected_cap
        if current_cap is not UNSET:
            field_dict["currentCap"] = current_cap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vote_v2_response import VoteV2Response

        d = dict(src_dict)
        id = d.pop("id")

        symbol = d.pop("symbol")

        expiry = d.pop("expiry")

        current_voter_apr = d.pop("currentVoterApr", UNSET)

        last_epoch_voter_apr = d.pop("lastEpochVoterApr", UNSET)

        current_swap_fee = d.pop("currentSwapFee", UNSET)

        last_epoch_swap_fee = d.pop("lastEpochSwapFee", UNSET)

        projected_voter_apr = d.pop("projectedVoterApr", UNSET)

        def _parse_projected_votes(data: object) -> Union["VoteV2Response", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                projected_votes_type_1 = VoteV2Response.from_dict(data)

                return projected_votes_type_1
            except:  # noqa: E722
                pass
            return cast(Union["VoteV2Response", None, Unset], data)

        projected_votes = _parse_projected_votes(d.pop("projectedVotes", UNSET))

        def _parse_current_votes(data: object) -> Union["VoteV2Response", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_votes_type_1 = VoteV2Response.from_dict(data)

                return current_votes_type_1
            except:  # noqa: E722
                pass
            return cast(Union["VoteV2Response", None, Unset], data)

        current_votes = _parse_current_votes(d.pop("currentVotes", UNSET))

        expected_cap = d.pop("expectedCap", UNSET)

        current_cap = d.pop("currentCap", UNSET)

        pool_v2_response = cls(
            id=id,
            symbol=symbol,
            expiry=expiry,
            current_voter_apr=current_voter_apr,
            last_epoch_voter_apr=last_epoch_voter_apr,
            current_swap_fee=current_swap_fee,
            last_epoch_swap_fee=last_epoch_swap_fee,
            projected_voter_apr=projected_voter_apr,
            projected_votes=projected_votes,
            current_votes=current_votes,
            expected_cap=expected_cap,
            current_cap=current_cap,
        )

        pool_v2_response.additional_properties = d
        return pool_v2_response

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
