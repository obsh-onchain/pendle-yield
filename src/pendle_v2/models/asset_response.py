import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.valuation_response import ValuationResponse


T = TypeVar("T", bound="AssetResponse")


@_attrs_define
class AssetResponse:
    """
    Attributes:
        id (str):
        chain_id (float):
        address (str):
        symbol (str):
        decimals (float):
        name (str):
        base_type (str):
        types (list[str]):
        simple_name (str):
        simple_symbol (str):
        simple_icon (str):
        pro_name (str):
        expiry (Union[None, Unset, datetime.datetime]):
        accent_color (Union[None, Unset, str]):
        price (Union['ValuationResponse', None, Unset]):
        price_updated_at (Union[None, Unset, datetime.datetime]):
        protocol (Union[None, Unset, str]):
        underlying_pool (Union[None, Unset, str]):
        pro_symbol (Union[None, Unset, str]):
        pro_icon (Union[None, Unset, str]):
        zappable (Union[None, Unset, bool]):
    """

    id: str
    chain_id: float
    address: str
    symbol: str
    decimals: float
    name: str
    base_type: str
    types: list[str]
    simple_name: str
    simple_symbol: str
    simple_icon: str
    pro_name: str
    expiry: Union[None, Unset, datetime.datetime] = UNSET
    accent_color: Union[None, Unset, str] = UNSET
    price: Union["ValuationResponse", None, Unset] = UNSET
    price_updated_at: Union[None, Unset, datetime.datetime] = UNSET
    protocol: Union[None, Unset, str] = UNSET
    underlying_pool: Union[None, Unset, str] = UNSET
    pro_symbol: Union[None, Unset, str] = UNSET
    pro_icon: Union[None, Unset, str] = UNSET
    zappable: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.valuation_response import ValuationResponse

        id = self.id

        chain_id = self.chain_id

        address = self.address

        symbol = self.symbol

        decimals = self.decimals

        name = self.name

        base_type = self.base_type

        types = self.types

        simple_name = self.simple_name

        simple_symbol = self.simple_symbol

        simple_icon = self.simple_icon

        pro_name = self.pro_name

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

        pro_symbol: Union[None, Unset, str]
        if isinstance(self.pro_symbol, Unset):
            pro_symbol = UNSET
        else:
            pro_symbol = self.pro_symbol

        pro_icon: Union[None, Unset, str]
        if isinstance(self.pro_icon, Unset):
            pro_icon = UNSET
        else:
            pro_icon = self.pro_icon

        zappable: Union[None, Unset, bool]
        if isinstance(self.zappable, Unset):
            zappable = UNSET
        else:
            zappable = self.zappable

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
                "baseType": base_type,
                "types": types,
                "simpleName": simple_name,
                "simpleSymbol": simple_symbol,
                "simpleIcon": simple_icon,
                "proName": pro_name,
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
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if underlying_pool is not UNSET:
            field_dict["underlyingPool"] = underlying_pool
        if pro_symbol is not UNSET:
            field_dict["proSymbol"] = pro_symbol
        if pro_icon is not UNSET:
            field_dict["proIcon"] = pro_icon
        if zappable is not UNSET:
            field_dict["zappable"] = zappable

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

        base_type = d.pop("baseType")

        types = cast(list[str], d.pop("types"))

        simple_name = d.pop("simpleName")

        simple_symbol = d.pop("simpleSymbol")

        simple_icon = d.pop("simpleIcon")

        pro_name = d.pop("proName")

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

        def _parse_pro_symbol(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pro_symbol = _parse_pro_symbol(d.pop("proSymbol", UNSET))

        def _parse_pro_icon(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pro_icon = _parse_pro_icon(d.pop("proIcon", UNSET))

        def _parse_zappable(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        zappable = _parse_zappable(d.pop("zappable", UNSET))

        asset_response = cls(
            id=id,
            chain_id=chain_id,
            address=address,
            symbol=symbol,
            decimals=decimals,
            name=name,
            base_type=base_type,
            types=types,
            simple_name=simple_name,
            simple_symbol=simple_symbol,
            simple_icon=simple_icon,
            pro_name=pro_name,
            expiry=expiry,
            accent_color=accent_color,
            price=price,
            price_updated_at=price_updated_at,
            protocol=protocol,
            underlying_pool=underlying_pool,
            pro_symbol=pro_symbol,
            pro_icon=pro_icon,
            zappable=zappable,
        )

        asset_response.additional_properties = d
        return asset_response

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
