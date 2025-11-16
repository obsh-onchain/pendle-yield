from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_monthly_revenue_response import GetMonthlyRevenueResponse
    from ..models.pendle_token_supply_response import PendleTokenSupplyResponse
    from ..models.pool_v2_response import PoolV2Response


T = TypeVar("T", bound="VePendleExtendedDataResponse")


@_attrs_define
class VePendleExtendedDataResponse:
    """
    Attributes:
        avg_lock_duration (float): Average lock duration in days
        total_pendle_locked (float): Total amount of PENDLE tokens locked in vePENDLE
        ve_pendle_supply (float): Total supply of vePENDLE tokens
        total_projected_votes (float): Total projected votes for next epoch
        total_current_votes (float): Total votes in current epoch
        pools (list['PoolV2Response']): List of voting pools with their APY, fees, and voting data
        token_supply (Union[Unset, PendleTokenSupplyResponse]):
        monthly_revenue (Union[Unset, GetMonthlyRevenueResponse]):
    """

    avg_lock_duration: float
    total_pendle_locked: float
    ve_pendle_supply: float
    total_projected_votes: float
    total_current_votes: float
    pools: list["PoolV2Response"]
    token_supply: Union[Unset, "PendleTokenSupplyResponse"] = UNSET
    monthly_revenue: Union[Unset, "GetMonthlyRevenueResponse"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_lock_duration = self.avg_lock_duration

        total_pendle_locked = self.total_pendle_locked

        ve_pendle_supply = self.ve_pendle_supply

        total_projected_votes = self.total_projected_votes

        total_current_votes = self.total_current_votes

        pools = []
        for pools_item_data in self.pools:
            pools_item = pools_item_data.to_dict()
            pools.append(pools_item)

        token_supply: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.token_supply, Unset):
            token_supply = self.token_supply.to_dict()

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
                "totalProjectedVotes": total_projected_votes,
                "totalCurrentVotes": total_current_votes,
                "pools": pools,
            }
        )
        if token_supply is not UNSET:
            field_dict["tokenSupply"] = token_supply
        if monthly_revenue is not UNSET:
            field_dict["monthlyRevenue"] = monthly_revenue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_monthly_revenue_response import GetMonthlyRevenueResponse
        from ..models.pendle_token_supply_response import PendleTokenSupplyResponse
        from ..models.pool_v2_response import PoolV2Response

        d = dict(src_dict)
        avg_lock_duration = d.pop("avgLockDuration")

        total_pendle_locked = d.pop("totalPendleLocked")

        ve_pendle_supply = d.pop("vePendleSupply")

        total_projected_votes = d.pop("totalProjectedVotes")

        total_current_votes = d.pop("totalCurrentVotes")

        pools = []
        _pools = d.pop("pools")
        for pools_item_data in _pools:
            pools_item = PoolV2Response.from_dict(pools_item_data)

            pools.append(pools_item)

        _token_supply = d.pop("tokenSupply", UNSET)
        token_supply: Union[Unset, PendleTokenSupplyResponse]
        if isinstance(_token_supply, Unset):
            token_supply = UNSET
        else:
            token_supply = PendleTokenSupplyResponse.from_dict(_token_supply)

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
            total_projected_votes=total_projected_votes,
            total_current_votes=total_current_votes,
            pools=pools,
            token_supply=token_supply,
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
