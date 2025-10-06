from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PoolResponse")


@_attrs_define
class PoolResponse:
    """
    Attributes:
        id (str):
        chain_id (float):
        address (str):
        symbol (str):
        expiry (str):
        voter_apy (float):
        name (str):
        farm_simple_name (str):
        farm_simple_icon (str):
        farm_pro_name (str):
        farm_pro_icon (str):
        protocol (Union[None, Unset, str]):
        underlying_pool (Union[None, Unset, str]):
        accent_color (Union[None, Unset, str]):
    """

    id: str
    chain_id: float
    address: str
    symbol: str
    expiry: str
    voter_apy: float
    name: str
    farm_simple_name: str
    farm_simple_icon: str
    farm_pro_name: str
    farm_pro_icon: str
    protocol: Union[None, Unset, str] = UNSET
    underlying_pool: Union[None, Unset, str] = UNSET
    accent_color: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        chain_id = self.chain_id

        address = self.address

        symbol = self.symbol

        expiry = self.expiry

        voter_apy = self.voter_apy

        name = self.name

        farm_simple_name = self.farm_simple_name

        farm_simple_icon = self.farm_simple_icon

        farm_pro_name = self.farm_pro_name

        farm_pro_icon = self.farm_pro_icon

        protocol: Union[None, Unset, str]
        if isinstance(self.protocol, Unset):
            protocol = UNSET
        else:
            protocol = self.protocol

        underlying_pool: Union[None, Unset, str]
        if isinstance(self.underlying_pool, Unset):
            underlying_pool = UNSET
        else:
            underlying_pool = self.underlying_pool

        accent_color: Union[None, Unset, str]
        if isinstance(self.accent_color, Unset):
            accent_color = UNSET
        else:
            accent_color = self.accent_color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "chainId": chain_id,
                "address": address,
                "symbol": symbol,
                "expiry": expiry,
                "voterApy": voter_apy,
                "name": name,
                "farmSimpleName": farm_simple_name,
                "farmSimpleIcon": farm_simple_icon,
                "farmProName": farm_pro_name,
                "farmProIcon": farm_pro_icon,
            }
        )
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if underlying_pool is not UNSET:
            field_dict["underlyingPool"] = underlying_pool
        if accent_color is not UNSET:
            field_dict["accentColor"] = accent_color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        chain_id = d.pop("chainId")

        address = d.pop("address")

        symbol = d.pop("symbol")

        expiry = d.pop("expiry")

        voter_apy = d.pop("voterApy")

        name = d.pop("name")

        farm_simple_name = d.pop("farmSimpleName")

        farm_simple_icon = d.pop("farmSimpleIcon")

        farm_pro_name = d.pop("farmProName")

        farm_pro_icon = d.pop("farmProIcon")

        def _parse_protocol(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        protocol = _parse_protocol(d.pop("protocol", UNSET))

        def _parse_underlying_pool(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        underlying_pool = _parse_underlying_pool(d.pop("underlyingPool", UNSET))

        def _parse_accent_color(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        accent_color = _parse_accent_color(d.pop("accentColor", UNSET))

        pool_response = cls(
            id=id,
            chain_id=chain_id,
            address=address,
            symbol=symbol,
            expiry=expiry,
            voter_apy=voter_apy,
            name=name,
            farm_simple_name=farm_simple_name,
            farm_simple_icon=farm_simple_icon,
            farm_pro_name=farm_pro_name,
            farm_pro_icon=farm_pro_icon,
            protocol=protocol,
            underlying_pool=underlying_pool,
            accent_color=accent_color,
        )

        pool_response.additional_properties = d
        return pool_response

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
