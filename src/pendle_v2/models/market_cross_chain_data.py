import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.market_details import MarketDetails


T = TypeVar("T", bound="MarketCrossChainData")


@_attrs_define
class MarketCrossChainData:
    """
    Attributes:
        name (str): market name Example: crvUSD.
        address (str): market address Example: 0x386f90eb964a477498b528a39d9405e73ed4032b.
        expiry (str): market expiry date Example: 2024-03-28T00:00:00.000Z.
        pt (str): market pt id Example: 1-0xb87511364014c088e30f872efc4a00d7efb843ac.
        yt (str): market yt id Example: 1-0xed97f94dd94255637a054098604e0201c442a3fd.
        sy (str): market sy id Example: 1-0xe05082b184a34668cd8a904d85fa815802bbb04c.
        underlying_asset (str): market underlying asset id Example: 1-0xa663b02cf0a4b149d2ad41910cb81e23e1c41c32.
        details (MarketDetails):
        is_new (bool): Whether the market is new
        is_prime (bool): Whether the market is prime
        timestamp (datetime.datetime): Market deployed timestamp
        chain_id (float): chain id Example: 1.
        lp_wrapper (Union[Unset, str]): LP wrapper address
        category_ids (Union[Unset, list[str]]): Market category IDs Example: ['btc', 'stables'].
    """

    name: str
    address: str
    expiry: str
    pt: str
    yt: str
    sy: str
    underlying_asset: str
    details: "MarketDetails"
    is_new: bool
    is_prime: bool
    timestamp: datetime.datetime
    chain_id: float
    lp_wrapper: Union[Unset, str] = UNSET
    category_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        address = self.address

        expiry = self.expiry

        pt = self.pt

        yt = self.yt

        sy = self.sy

        underlying_asset = self.underlying_asset

        details = self.details.to_dict()

        is_new = self.is_new

        is_prime = self.is_prime

        timestamp = self.timestamp.isoformat()

        chain_id = self.chain_id

        lp_wrapper = self.lp_wrapper

        category_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.category_ids, Unset):
            category_ids = self.category_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "address": address,
                "expiry": expiry,
                "pt": pt,
                "yt": yt,
                "sy": sy,
                "underlyingAsset": underlying_asset,
                "details": details,
                "isNew": is_new,
                "isPrime": is_prime,
                "timestamp": timestamp,
                "chainId": chain_id,
            }
        )
        if lp_wrapper is not UNSET:
            field_dict["lpWrapper"] = lp_wrapper
        if category_ids is not UNSET:
            field_dict["categoryIds"] = category_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market_details import MarketDetails

        d = dict(src_dict)
        name = d.pop("name")

        address = d.pop("address")

        expiry = d.pop("expiry")

        pt = d.pop("pt")

        yt = d.pop("yt")

        sy = d.pop("sy")

        underlying_asset = d.pop("underlyingAsset")

        details = MarketDetails.from_dict(d.pop("details"))

        is_new = d.pop("isNew")

        is_prime = d.pop("isPrime")

        timestamp = isoparse(d.pop("timestamp"))

        chain_id = d.pop("chainId")

        lp_wrapper = d.pop("lpWrapper", UNSET)

        category_ids = cast(list[str], d.pop("categoryIds", UNSET))

        market_cross_chain_data = cls(
            name=name,
            address=address,
            expiry=expiry,
            pt=pt,
            yt=yt,
            sy=sy,
            underlying_asset=underlying_asset,
            details=details,
            is_new=is_new,
            is_prime=is_prime,
            timestamp=timestamp,
            chain_id=chain_id,
            lp_wrapper=lp_wrapper,
            category_ids=category_ids,
        )

        market_cross_chain_data.additional_properties = d
        return market_cross_chain_data

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
