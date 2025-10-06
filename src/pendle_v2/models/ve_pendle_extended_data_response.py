import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_monthly_revenue_response import GetMonthlyRevenueResponse
    from ..models.get_ongoing_votes_response import GetOngoingVotesResponse
    from ..models.get_ve_pendle_cap_response import GetVePendleCapResponse
    from ..models.pendle_token_supply_response import PendleTokenSupplyResponse
    from ..models.pool_response import PoolResponse
    from ..models.pool_v2_response import PoolV2Response
    from ..models.pool_voter_aprs_swap_fees_response import PoolVoterAprsSwapFeesResponse
    from ..models.ve_pendle_extended_data_response_month_airdrop_breakdown_item import (
        VePendleExtendedDataResponseMonthAirdropBreakdownItem,
    )
    from ..models.vote_snapshot_response import VoteSnapshotResponse


T = TypeVar("T", bound="VePendleExtendedDataResponse")


@_attrs_define
class VePendleExtendedDataResponse:
    """
    Attributes:
        avg_lock_duration (float): Average lock duration in days
        total_pendle_locked (float):
        ve_pendle_supply (float):
        month_total_swap_fee (float):
        airdrop_from_date (datetime.datetime):
        month_airdrop_breakdown (list['VePendleExtendedDataResponseMonthAirdropBreakdownItem']):
        total_projected_votes (float):
        total_current_votes (float):
        pools (list['PoolV2Response']):
        vote_snapshot (Union[Unset, VoteSnapshotResponse]):
        pool_voter_data (Union[Unset, PoolVoterAprsSwapFeesResponse]):
        pool_metadata (Union[Unset, list['PoolResponse']]): Metadata for all voting pools
        token_supply (Union[Unset, PendleTokenSupplyResponse]):
        ongoing_votes (Union[Unset, GetOngoingVotesResponse]):
        ve_pendle_cap (Union[Unset, GetVePendleCapResponse]):
        monthly_revenue (Union[Unset, GetMonthlyRevenueResponse]):
    """

    avg_lock_duration: float
    total_pendle_locked: float
    ve_pendle_supply: float
    month_total_swap_fee: float
    airdrop_from_date: datetime.datetime
    month_airdrop_breakdown: list["VePendleExtendedDataResponseMonthAirdropBreakdownItem"]
    total_projected_votes: float
    total_current_votes: float
    pools: list["PoolV2Response"]
    vote_snapshot: Union[Unset, "VoteSnapshotResponse"] = UNSET
    pool_voter_data: Union[Unset, "PoolVoterAprsSwapFeesResponse"] = UNSET
    pool_metadata: Union[Unset, list["PoolResponse"]] = UNSET
    token_supply: Union[Unset, "PendleTokenSupplyResponse"] = UNSET
    ongoing_votes: Union[Unset, "GetOngoingVotesResponse"] = UNSET
    ve_pendle_cap: Union[Unset, "GetVePendleCapResponse"] = UNSET
    monthly_revenue: Union[Unset, "GetMonthlyRevenueResponse"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_lock_duration = self.avg_lock_duration

        total_pendle_locked = self.total_pendle_locked

        ve_pendle_supply = self.ve_pendle_supply

        month_total_swap_fee = self.month_total_swap_fee

        airdrop_from_date = self.airdrop_from_date.isoformat()

        month_airdrop_breakdown = []
        for month_airdrop_breakdown_item_data in self.month_airdrop_breakdown:
            month_airdrop_breakdown_item = month_airdrop_breakdown_item_data.to_dict()
            month_airdrop_breakdown.append(month_airdrop_breakdown_item)

        total_projected_votes = self.total_projected_votes

        total_current_votes = self.total_current_votes

        pools = []
        for pools_item_data in self.pools:
            pools_item = pools_item_data.to_dict()
            pools.append(pools_item)

        vote_snapshot: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vote_snapshot, Unset):
            vote_snapshot = self.vote_snapshot.to_dict()

        pool_voter_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pool_voter_data, Unset):
            pool_voter_data = self.pool_voter_data.to_dict()

        pool_metadata: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.pool_metadata, Unset):
            pool_metadata = []
            for pool_metadata_item_data in self.pool_metadata:
                pool_metadata_item = pool_metadata_item_data.to_dict()
                pool_metadata.append(pool_metadata_item)

        token_supply: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.token_supply, Unset):
            token_supply = self.token_supply.to_dict()

        ongoing_votes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ongoing_votes, Unset):
            ongoing_votes = self.ongoing_votes.to_dict()

        ve_pendle_cap: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ve_pendle_cap, Unset):
            ve_pendle_cap = self.ve_pendle_cap.to_dict()

        monthly_revenue: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.monthly_revenue, Unset):
            monthly_revenue = self.monthly_revenue.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avgLockDuration": avg_lock_duration,
                "totalPendleLocked": total_pendle_locked,
                "vePendleSupply": ve_pendle_supply,
                "monthTotalSwapFee": month_total_swap_fee,
                "airdropFromDate": airdrop_from_date,
                "monthAirdropBreakdown": month_airdrop_breakdown,
                "totalProjectedVotes": total_projected_votes,
                "totalCurrentVotes": total_current_votes,
                "pools": pools,
            }
        )
        if vote_snapshot is not UNSET:
            field_dict["voteSnapshot"] = vote_snapshot
        if pool_voter_data is not UNSET:
            field_dict["poolVoterData"] = pool_voter_data
        if pool_metadata is not UNSET:
            field_dict["poolMetadata"] = pool_metadata
        if token_supply is not UNSET:
            field_dict["tokenSupply"] = token_supply
        if ongoing_votes is not UNSET:
            field_dict["ongoingVotes"] = ongoing_votes
        if ve_pendle_cap is not UNSET:
            field_dict["vePendleCap"] = ve_pendle_cap
        if monthly_revenue is not UNSET:
            field_dict["monthlyRevenue"] = monthly_revenue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_monthly_revenue_response import GetMonthlyRevenueResponse
        from ..models.get_ongoing_votes_response import GetOngoingVotesResponse
        from ..models.get_ve_pendle_cap_response import GetVePendleCapResponse
        from ..models.pendle_token_supply_response import PendleTokenSupplyResponse
        from ..models.pool_response import PoolResponse
        from ..models.pool_v2_response import PoolV2Response
        from ..models.pool_voter_aprs_swap_fees_response import PoolVoterAprsSwapFeesResponse
        from ..models.ve_pendle_extended_data_response_month_airdrop_breakdown_item import (
            VePendleExtendedDataResponseMonthAirdropBreakdownItem,
        )
        from ..models.vote_snapshot_response import VoteSnapshotResponse

        d = dict(src_dict)
        avg_lock_duration = d.pop("avgLockDuration")

        total_pendle_locked = d.pop("totalPendleLocked")

        ve_pendle_supply = d.pop("vePendleSupply")

        month_total_swap_fee = d.pop("monthTotalSwapFee")

        airdrop_from_date = isoparse(d.pop("airdropFromDate"))

        month_airdrop_breakdown = []
        _month_airdrop_breakdown = d.pop("monthAirdropBreakdown")
        for month_airdrop_breakdown_item_data in _month_airdrop_breakdown:
            month_airdrop_breakdown_item = VePendleExtendedDataResponseMonthAirdropBreakdownItem.from_dict(
                month_airdrop_breakdown_item_data
            )

            month_airdrop_breakdown.append(month_airdrop_breakdown_item)

        total_projected_votes = d.pop("totalProjectedVotes")

        total_current_votes = d.pop("totalCurrentVotes")

        pools = []
        _pools = d.pop("pools")
        for pools_item_data in _pools:
            pools_item = PoolV2Response.from_dict(pools_item_data)

            pools.append(pools_item)

        _vote_snapshot = d.pop("voteSnapshot", UNSET)
        vote_snapshot: Union[Unset, VoteSnapshotResponse]
        if isinstance(_vote_snapshot, Unset):
            vote_snapshot = UNSET
        else:
            vote_snapshot = VoteSnapshotResponse.from_dict(_vote_snapshot)

        _pool_voter_data = d.pop("poolVoterData", UNSET)
        pool_voter_data: Union[Unset, PoolVoterAprsSwapFeesResponse]
        if isinstance(_pool_voter_data, Unset):
            pool_voter_data = UNSET
        else:
            pool_voter_data = PoolVoterAprsSwapFeesResponse.from_dict(_pool_voter_data)

        pool_metadata = []
        _pool_metadata = d.pop("poolMetadata", UNSET)
        for pool_metadata_item_data in _pool_metadata or []:
            pool_metadata_item = PoolResponse.from_dict(pool_metadata_item_data)

            pool_metadata.append(pool_metadata_item)

        _token_supply = d.pop("tokenSupply", UNSET)
        token_supply: Union[Unset, PendleTokenSupplyResponse]
        if isinstance(_token_supply, Unset):
            token_supply = UNSET
        else:
            token_supply = PendleTokenSupplyResponse.from_dict(_token_supply)

        _ongoing_votes = d.pop("ongoingVotes", UNSET)
        ongoing_votes: Union[Unset, GetOngoingVotesResponse]
        if isinstance(_ongoing_votes, Unset):
            ongoing_votes = UNSET
        else:
            ongoing_votes = GetOngoingVotesResponse.from_dict(_ongoing_votes)

        _ve_pendle_cap = d.pop("vePendleCap", UNSET)
        ve_pendle_cap: Union[Unset, GetVePendleCapResponse]
        if isinstance(_ve_pendle_cap, Unset):
            ve_pendle_cap = UNSET
        else:
            ve_pendle_cap = GetVePendleCapResponse.from_dict(_ve_pendle_cap)

        _monthly_revenue = d.pop("monthlyRevenue", UNSET)
        monthly_revenue: Union[Unset, GetMonthlyRevenueResponse]
        if isinstance(_monthly_revenue, Unset):
            monthly_revenue = UNSET
        else:
            monthly_revenue = GetMonthlyRevenueResponse.from_dict(_monthly_revenue)

        ve_pendle_extended_data_response = cls(
            avg_lock_duration=avg_lock_duration,
            total_pendle_locked=total_pendle_locked,
            ve_pendle_supply=ve_pendle_supply,
            month_total_swap_fee=month_total_swap_fee,
            airdrop_from_date=airdrop_from_date,
            month_airdrop_breakdown=month_airdrop_breakdown,
            total_projected_votes=total_projected_votes,
            total_current_votes=total_current_votes,
            pools=pools,
            vote_snapshot=vote_snapshot,
            pool_voter_data=pool_voter_data,
            pool_metadata=pool_metadata,
            token_supply=token_supply,
            ongoing_votes=ongoing_votes,
            ve_pendle_cap=ve_pendle_cap,
            monthly_revenue=monthly_revenue,
        )

        ve_pendle_extended_data_response.additional_properties = d
        return ve_pendle_extended_data_response

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
