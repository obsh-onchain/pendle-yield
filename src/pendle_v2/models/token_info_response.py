from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.token_info_response_extensions import TokenInfoResponseExtensions


T = TypeVar("T", bound="TokenInfoResponse")


@_attrs_define
class TokenInfoResponse:
    """
    Attributes:
        chain_id (float):
        address (str):
        decimals (float):
        name (str):
        symbol (str):
        logo_uri (str):
        tags (list[str]):
        extensions (TokenInfoResponseExtensions):
    """

    chain_id: float
    address: str
    decimals: float
    name: str
    symbol: str
    logo_uri: str
    tags: list[str]
    extensions: "TokenInfoResponseExtensions"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chain_id = self.chain_id

        address = self.address

        decimals = self.decimals

        name = self.name

        symbol = self.symbol

        logo_uri = self.logo_uri

        tags = self.tags

        extensions = self.extensions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chainId": chain_id,
                "address": address,
                "decimals": decimals,
                "name": name,
                "symbol": symbol,
                "logoURI": logo_uri,
                "tags": tags,
                "extensions": extensions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_info_response_extensions import TokenInfoResponseExtensions

        d = dict(src_dict)
        chain_id = d.pop("chainId")

        address = d.pop("address")

        decimals = d.pop("decimals")

        name = d.pop("name")

        symbol = d.pop("symbol")

        logo_uri = d.pop("logoURI")

        tags = cast(list[str], d.pop("tags"))

        extensions = TokenInfoResponseExtensions.from_dict(d.pop("extensions"))

        token_info_response = cls(
            chain_id=chain_id,
            address=address,
            decimals=decimals,
            name=name,
            symbol=symbol,
            logo_uri=logo_uri,
            tags=tags,
            extensions=extensions,
        )

        token_info_response.additional_properties = d
        return token_info_response

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
