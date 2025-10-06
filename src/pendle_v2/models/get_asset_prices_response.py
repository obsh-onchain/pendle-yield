from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_asset_prices_response_prices import GetAssetPricesResponsePrices


T = TypeVar("T", bound="GetAssetPricesResponse")


@_attrs_define
class GetAssetPricesResponse:
    """
    Attributes:
        prices (GetAssetPricesResponsePrices):  Example: {'0x5fe30ac5cb1abb0e44cdffb2916c254aeb368650':
            0.9989673642973003, '0xd393d1ddd6b8811a86d925f5e14014282581bc04': 1.001712}.
        total (float): Total number of assets
        skip (float): Number of assets got skipped
        limit (Union[None, Unset, float]): Number of assets limited by the query
    """

    prices: "GetAssetPricesResponsePrices"
    total: float
    skip: float
    limit: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prices = self.prices.to_dict()

        total = self.total

        skip = self.skip

        limit: Union[None, Unset, float]
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prices": prices,
                "total": total,
                "skip": skip,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_asset_prices_response_prices import GetAssetPricesResponsePrices

        d = dict(src_dict)
        prices = GetAssetPricesResponsePrices.from_dict(d.pop("prices"))

        total = d.pop("total")

        skip = d.pop("skip")

        def _parse_limit(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        limit = _parse_limit(d.pop("limit", UNSET))

        get_asset_prices_response = cls(
            prices=prices,
            total=total,
            skip=skip,
            limit=limit,
        )

        get_asset_prices_response.additional_properties = d
        return get_asset_prices_response

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
