from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.liquid_locker_pool_response import LiquidLockerPoolResponse
    from ..models.wlp_distinct_users_response import WlpDistinctUsersResponse
    from ..models.wlp_holder_mapping_response import WlpHolderMappingResponse


T = TypeVar("T", bound="GetAllRelatedInfoFromLpAndWlpResponse")


@_attrs_define
class GetAllRelatedInfoFromLpAndWlpResponse:
    """
    Attributes:
        distinct_users (list[str]): Distinct users for the LP token
        liquid_locker_pools (list['LiquidLockerPoolResponse']): Liquid locker pools info for LP token
        wlp_distinct_users_response (WlpDistinctUsersResponse):
        wlp_holder_mappings (list['WlpHolderMappingResponse']): WLP holder mappings for WLP token
    """

    distinct_users: list[str]
    liquid_locker_pools: list["LiquidLockerPoolResponse"]
    wlp_distinct_users_response: "WlpDistinctUsersResponse"
    wlp_holder_mappings: list["WlpHolderMappingResponse"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        distinct_users = self.distinct_users

        liquid_locker_pools = []
        for liquid_locker_pools_item_data in self.liquid_locker_pools:
            liquid_locker_pools_item = liquid_locker_pools_item_data.to_dict()
            liquid_locker_pools.append(liquid_locker_pools_item)

        wlp_distinct_users_response = self.wlp_distinct_users_response.to_dict()

        wlp_holder_mappings = []
        for wlp_holder_mappings_item_data in self.wlp_holder_mappings:
            wlp_holder_mappings_item = wlp_holder_mappings_item_data.to_dict()
            wlp_holder_mappings.append(wlp_holder_mappings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "distinctUsers": distinct_users,
                "liquidLockerPools": liquid_locker_pools,
                "wlpDistinctUsersResponse": wlp_distinct_users_response,
                "wlpHolderMappings": wlp_holder_mappings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.liquid_locker_pool_response import LiquidLockerPoolResponse
        from ..models.wlp_distinct_users_response import WlpDistinctUsersResponse
        from ..models.wlp_holder_mapping_response import WlpHolderMappingResponse

        d = dict(src_dict)
        distinct_users = cast(list[str], d.pop("distinctUsers"))

        liquid_locker_pools = []
        _liquid_locker_pools = d.pop("liquidLockerPools")
        for liquid_locker_pools_item_data in _liquid_locker_pools:
            liquid_locker_pools_item = LiquidLockerPoolResponse.from_dict(liquid_locker_pools_item_data)

            liquid_locker_pools.append(liquid_locker_pools_item)

        wlp_distinct_users_response = WlpDistinctUsersResponse.from_dict(d.pop("wlpDistinctUsersResponse"))

        wlp_holder_mappings = []
        _wlp_holder_mappings = d.pop("wlpHolderMappings")
        for wlp_holder_mappings_item_data in _wlp_holder_mappings:
            wlp_holder_mappings_item = WlpHolderMappingResponse.from_dict(wlp_holder_mappings_item_data)

            wlp_holder_mappings.append(wlp_holder_mappings_item)

        get_all_related_info_from_lp_and_wlp_response = cls(
            distinct_users=distinct_users,
            liquid_locker_pools=liquid_locker_pools,
            wlp_distinct_users_response=wlp_distinct_users_response,
            wlp_holder_mappings=wlp_holder_mappings,
        )

        get_all_related_info_from_lp_and_wlp_response.additional_properties = d
        return get_all_related_info_from_lp_and_wlp_response

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
