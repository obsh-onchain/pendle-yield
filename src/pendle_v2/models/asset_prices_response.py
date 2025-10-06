from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssetPricesResponse")


@_attrs_define
class AssetPricesResponse:
    """
    Attributes:
        total (float): The number of assets returned
        addresses (list[str]): Addresses of returned assets, can be mapped by index with priceUsd array
        prices_usd (list[Union[None, float]]): Price in usd of mapped asset, can be mapped by index with addresses
            array, return null if the asset doesnt have price Example: [1, 2, None, 4].
    """

    total: float
    addresses: list[str]
    prices_usd: list[Union[None, float]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        addresses = self.addresses

        prices_usd = []
        for prices_usd_item_data in self.prices_usd:
            prices_usd_item: Union[None, float]
            prices_usd_item = prices_usd_item_data
            prices_usd.append(prices_usd_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "addresses": addresses,
                "pricesUsd": prices_usd,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        addresses = cast(list[str], d.pop("addresses"))

        prices_usd = []
        _prices_usd = d.pop("pricesUsd")
        for prices_usd_item_data in _prices_usd:

            def _parse_prices_usd_item(data: object) -> Union[None, float]:
                if data is None:
                    return data
                return cast(Union[None, float], data)

            prices_usd_item = _parse_prices_usd_item(prices_usd_item_data)

            prices_usd.append(prices_usd_item)

        asset_prices_response = cls(
            total=total,
            addresses=addresses,
            prices_usd=prices_usd,
        )

        asset_prices_response.additional_properties = d
        return asset_prices_response

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
