import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.valuation_response import ValuationResponse


T = TypeVar("T", bound="AssetBasicResponse")


@_attrs_define
class AssetBasicResponse:
    """
    Attributes:
        id (str):
        chain_id (float):
        address (str):
        symbol (str):
        decimals (float):
        name (str):
        expiry (Union[None, Unset, datetime.datetime]):
        accent_color (Union[None, Unset, str]):
        price (Union['ValuationResponse', None, Unset]):
        price_updated_at (Union[None, Unset, datetime.datetime]):
    """

    id: str
    chain_id: float
    address: str
    symbol: str
    decimals: float
    name: str
    expiry: Union[None, Unset, datetime.datetime] = UNSET
    accent_color: Union[None, Unset, str] = UNSET
    price: Union["ValuationResponse", None, Unset] = UNSET
    price_updated_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.valuation_response import ValuationResponse

        id = self.id

        chain_id = self.chain_id

        address = self.address

        symbol = self.symbol

        decimals = self.decimals

        name = self.name

        expiry: Union[None, Unset, str]
        if isinstance(self.expiry, Unset):
            expiry = UNSET
        elif isinstance(self.expiry, datetime.datetime):
            expiry = self.expiry.isoformat()
        else:
            expiry = self.expiry

        accent_color: Union[None, Unset, str]
        if isinstance(self.accent_color, Unset):
            accent_color = UNSET
        else:
            accent_color = self.accent_color

        price: Union[None, Unset, dict[str, Any]]
        if isinstance(self.price, Unset):
            price = UNSET
        elif isinstance(self.price, ValuationResponse):
            price = self.price.to_dict()
        else:
            price = self.price

        price_updated_at: Union[None, Unset, str]
        if isinstance(self.price_updated_at, Unset):
            price_updated_at = UNSET
        elif isinstance(self.price_updated_at, datetime.datetime):
            price_updated_at = self.price_updated_at.isoformat()
        else:
            price_updated_at = self.price_updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "chainId": chain_id,
                "address": address,
                "symbol": symbol,
                "decimals": decimals,
                "name": name,
            }
        )
        if expiry is not UNSET:
            field_dict["expiry"] = expiry
        if accent_color is not UNSET:
            field_dict["accentColor"] = accent_color
        if price is not UNSET:
            field_dict["price"] = price
        if price_updated_at is not UNSET:
            field_dict["priceUpdatedAt"] = price_updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.valuation_response import ValuationResponse

        d = dict(src_dict)
        id = d.pop("id")

        chain_id = d.pop("chainId")

        address = d.pop("address")

        symbol = d.pop("symbol")

        decimals = d.pop("decimals")

        name = d.pop("name")

        def _parse_expiry(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiry_type_0 = isoparse(data)

                return expiry_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expiry = _parse_expiry(d.pop("expiry", UNSET))

        def _parse_accent_color(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        accent_color = _parse_accent_color(d.pop("accentColor", UNSET))

        def _parse_price(data: object) -> Union["ValuationResponse", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                price_type_1 = ValuationResponse.from_dict(data)

                return price_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ValuationResponse", None, Unset], data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_price_updated_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                price_updated_at_type_0 = isoparse(data)

                return price_updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        price_updated_at = _parse_price_updated_at(d.pop("priceUpdatedAt", UNSET))

        asset_basic_response = cls(
            id=id,
            chain_id=chain_id,
            address=address,
            symbol=symbol,
            decimals=decimals,
            name=name,
            expiry=expiry,
            accent_color=accent_color,
            price=price,
            price_updated_at=price_updated_at,
        )

        asset_basic_response.additional_properties = d
        return asset_basic_response

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
