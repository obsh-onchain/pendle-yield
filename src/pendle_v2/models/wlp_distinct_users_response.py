from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.euler_user_response import EulerUserResponse
    from ..models.morpho_config_response import MorphoConfigResponse
    from ..models.morpho_user_response import MorphoUserResponse
    from ..models.silo_user_response import SiloUserResponse


T = TypeVar("T", bound="WlpDistinctUsersResponse")


@_attrs_define
class WlpDistinctUsersResponse:
    """
    Attributes:
        wlp_users_total (float): WLP token address
        euler_users_total (float): WLP token address
        morpho_users_total (float): WLP token address
        silo_users_total (float): WLP token address
        wlp_users (list[str]): Array of distinct user addresses that have interacted with WLP
        euler_users (list['EulerUserResponse']): Array of Euler users
        morpho_users (list['MorphoUserResponse']): Array of Morpho users
        silo_users (list['SiloUserResponse']): Array of Silo users
        wlp_address (str): WLP token address
        morpho_configs (list['MorphoConfigResponse']): Morpho config address
    """

    wlp_users_total: float
    euler_users_total: float
    morpho_users_total: float
    silo_users_total: float
    wlp_users: list[str]
    euler_users: list["EulerUserResponse"]
    morpho_users: list["MorphoUserResponse"]
    silo_users: list["SiloUserResponse"]
    wlp_address: str
    morpho_configs: list["MorphoConfigResponse"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wlp_users_total = self.wlp_users_total

        euler_users_total = self.euler_users_total

        morpho_users_total = self.morpho_users_total

        silo_users_total = self.silo_users_total

        wlp_users = self.wlp_users

        euler_users = []
        for euler_users_item_data in self.euler_users:
            euler_users_item = euler_users_item_data.to_dict()
            euler_users.append(euler_users_item)

        morpho_users = []
        for morpho_users_item_data in self.morpho_users:
            morpho_users_item = morpho_users_item_data.to_dict()
            morpho_users.append(morpho_users_item)

        silo_users = []
        for silo_users_item_data in self.silo_users:
            silo_users_item = silo_users_item_data.to_dict()
            silo_users.append(silo_users_item)

        wlp_address = self.wlp_address

        morpho_configs = []
        for morpho_configs_item_data in self.morpho_configs:
            morpho_configs_item = morpho_configs_item_data.to_dict()
            morpho_configs.append(morpho_configs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wlpUsersTotal": wlp_users_total,
                "eulerUsersTotal": euler_users_total,
                "morphoUsersTotal": morpho_users_total,
                "siloUsersTotal": silo_users_total,
                "wlpUsers": wlp_users,
                "eulerUsers": euler_users,
                "morphoUsers": morpho_users,
                "siloUsers": silo_users,
                "wlpAddress": wlp_address,
                "morphoConfigs": morpho_configs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.euler_user_response import EulerUserResponse
        from ..models.morpho_config_response import MorphoConfigResponse
        from ..models.morpho_user_response import MorphoUserResponse
        from ..models.silo_user_response import SiloUserResponse

        d = dict(src_dict)
        wlp_users_total = d.pop("wlpUsersTotal")

        euler_users_total = d.pop("eulerUsersTotal")

        morpho_users_total = d.pop("morphoUsersTotal")

        silo_users_total = d.pop("siloUsersTotal")

        wlp_users = cast(list[str], d.pop("wlpUsers"))

        euler_users = []
        _euler_users = d.pop("eulerUsers")
        for euler_users_item_data in _euler_users:
            euler_users_item = EulerUserResponse.from_dict(euler_users_item_data)

            euler_users.append(euler_users_item)

        morpho_users = []
        _morpho_users = d.pop("morphoUsers")
        for morpho_users_item_data in _morpho_users:
            morpho_users_item = MorphoUserResponse.from_dict(morpho_users_item_data)

            morpho_users.append(morpho_users_item)

        silo_users = []
        _silo_users = d.pop("siloUsers")
        for silo_users_item_data in _silo_users:
            silo_users_item = SiloUserResponse.from_dict(silo_users_item_data)

            silo_users.append(silo_users_item)

        wlp_address = d.pop("wlpAddress")

        morpho_configs = []
        _morpho_configs = d.pop("morphoConfigs")
        for morpho_configs_item_data in _morpho_configs:
            morpho_configs_item = MorphoConfigResponse.from_dict(morpho_configs_item_data)

            morpho_configs.append(morpho_configs_item)

        wlp_distinct_users_response = cls(
            wlp_users_total=wlp_users_total,
            euler_users_total=euler_users_total,
            morpho_users_total=morpho_users_total,
            silo_users_total=silo_users_total,
            wlp_users=wlp_users,
            euler_users=euler_users,
            morpho_users=morpho_users,
            silo_users=silo_users,
            wlp_address=wlp_address,
            morpho_configs=morpho_configs,
        )

        wlp_distinct_users_response.additional_properties = d
        return wlp_distinct_users_response

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
