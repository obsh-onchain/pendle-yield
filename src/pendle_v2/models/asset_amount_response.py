from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.asset_response import AssetResponse
    from ..models.valuation_response import ValuationResponse


T = TypeVar("T", bound="AssetAmountResponse")


@_attrs_define
class AssetAmountResponse:
    """
    Attributes:
        asset (AssetResponse):
        amount (float):
        price (ValuationResponse):
    """

    asset: "AssetResponse"
    amount: float
    price: "ValuationResponse"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset = self.asset.to_dict()

        amount = self.amount

        price = self.price.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset": asset,
                "amount": amount,
                "price": price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_response import AssetResponse
        from ..models.valuation_response import ValuationResponse

        d = dict(src_dict)
        asset = AssetResponse.from_dict(d.pop("asset"))

        amount = d.pop("amount")

        price = ValuationResponse.from_dict(d.pop("price"))

        asset_amount_response = cls(
            asset=asset,
            amount=amount,
            price=price,
        )

        asset_amount_response.additional_properties = d
        return asset_amount_response

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
