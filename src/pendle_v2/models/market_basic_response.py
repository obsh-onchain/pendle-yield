import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="MarketBasicResponse")


@_attrs_define
class MarketBasicResponse:
    """
    Attributes:
        id (str):
        chain_id (float):
        address (str):
        symbol (str):
        expiry (datetime.datetime):
        name (str):
    """

    id: str
    chain_id: float
    address: str
    symbol: str
    expiry: datetime.datetime
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        chain_id = self.chain_id

        address = self.address

        symbol = self.symbol

        expiry = self.expiry.isoformat()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "chainId": chain_id,
                "address": address,
                "symbol": symbol,
                "expiry": expiry,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        chain_id = d.pop("chainId")

        address = d.pop("address")

        symbol = d.pop("symbol")

        expiry = isoparse(d.pop("expiry"))

        name = d.pop("name")

        market_basic_response = cls(
            id=id,
            chain_id=chain_id,
            address=address,
            symbol=symbol,
            expiry=expiry,
            name=name,
        )

        market_basic_response.additional_properties = d
        return market_basic_response

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
