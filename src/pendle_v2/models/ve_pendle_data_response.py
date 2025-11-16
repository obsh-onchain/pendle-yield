from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pool_v2_response import PoolV2Response


T = TypeVar("T", bound="VePendleDataResponse")


@_attrs_define
class VePendleDataResponse:
    """
    Attributes:
        avg_lock_duration (float): Average lock duration in days
        total_pendle_locked (float): Total amount of PENDLE tokens locked in vePENDLE
        ve_pendle_supply (float): Total supply of vePENDLE tokens
        total_projected_votes (float): Total projected votes for next epoch
        total_current_votes (float): Total votes in current epoch
        pools (list['PoolV2Response']): List of voting pools with their APY, fees, and voting data
    """

    avg_lock_duration: float
    total_pendle_locked: float
    ve_pendle_supply: float
    total_projected_votes: float
    total_current_votes: float
    pools: list["PoolV2Response"]
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        ve_pendle_data_response = cls(
            avg_lock_duration=avg_lock_duration,
            total_pendle_locked=total_pendle_locked,
            ve_pendle_supply=ve_pendle_supply,
            total_projected_votes=total_projected_votes,
            total_current_votes=total_current_votes,
            pools=pools,
        )

        ve_pendle_data_response.additional_properties = d
        return ve_pendle_data_response

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
