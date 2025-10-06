from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.token_info_response import TokenInfoResponse
    from ..models.uniswap_token_list_response_tags import UniswapTokenListResponseTags
    from ..models.uniswap_token_list_response_token_map import UniswapTokenListResponseTokenMap
    from ..models.version_response import VersionResponse


T = TypeVar("T", bound="UniswapTokenListResponse")


@_attrs_define
class UniswapTokenListResponse:
    """
    Attributes:
        name (str):
        timestamp (str):
        version (VersionResponse):
        tokens (list['TokenInfoResponse']):
        token_map (UniswapTokenListResponseTokenMap):
        keywords (list[str]):
        logo_uri (str):
        tags (UniswapTokenListResponseTags):
    """

    name: str
    timestamp: str
    version: "VersionResponse"
    tokens: list["TokenInfoResponse"]
    token_map: "UniswapTokenListResponseTokenMap"
    keywords: list[str]
    logo_uri: str
    tags: "UniswapTokenListResponseTags"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        timestamp = self.timestamp

        version = self.version.to_dict()

        tokens = []
        for tokens_item_data in self.tokens:
            tokens_item = tokens_item_data.to_dict()
            tokens.append(tokens_item)

        token_map = self.token_map.to_dict()

        keywords = self.keywords

        logo_uri = self.logo_uri

        tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "timestamp": timestamp,
                "version": version,
                "tokens": tokens,
                "tokenMap": token_map,
                "keywords": keywords,
                "logoURI": logo_uri,
                "tags": tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_info_response import TokenInfoResponse
        from ..models.uniswap_token_list_response_tags import UniswapTokenListResponseTags
        from ..models.uniswap_token_list_response_token_map import UniswapTokenListResponseTokenMap
        from ..models.version_response import VersionResponse

        d = dict(src_dict)
        name = d.pop("name")

        timestamp = d.pop("timestamp")

        version = VersionResponse.from_dict(d.pop("version"))

        tokens = []
        _tokens = d.pop("tokens")
        for tokens_item_data in _tokens:
            tokens_item = TokenInfoResponse.from_dict(tokens_item_data)

            tokens.append(tokens_item)

        token_map = UniswapTokenListResponseTokenMap.from_dict(d.pop("tokenMap"))

        keywords = cast(list[str], d.pop("keywords"))

        logo_uri = d.pop("logoURI")

        tags = UniswapTokenListResponseTags.from_dict(d.pop("tags"))

        uniswap_token_list_response = cls(
            name=name,
            timestamp=timestamp,
            version=version,
            tokens=tokens,
            token_map=token_map,
            keywords=keywords,
            logo_uri=logo_uri,
            tags=tags,
        )

        uniswap_token_list_response.additional_properties = d
        return uniswap_token_list_response

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
