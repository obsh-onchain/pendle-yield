from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.asset_response import AssetResponse


T = TypeVar("T", bound="MarketAssetsResponse")


@_attrs_define
class MarketAssetsResponse:
    """
    Attributes:
        pt (AssetResponse):
        yt (AssetResponse):
        sy (AssetResponse):
        lp (AssetResponse):
        accounting_asset (AssetResponse):
        underlying_asset (AssetResponse):
        base_pricing_asset (AssetResponse):
        reward_tokens (list['AssetResponse']):
        input_tokens (list['AssetResponse']):
        output_tokens (list['AssetResponse']):
    """

    pt: "AssetResponse"
    yt: "AssetResponse"
    sy: "AssetResponse"
    lp: "AssetResponse"
    accounting_asset: "AssetResponse"
    underlying_asset: "AssetResponse"
    base_pricing_asset: "AssetResponse"
    reward_tokens: list["AssetResponse"]
    input_tokens: list["AssetResponse"]
    output_tokens: list["AssetResponse"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pt = self.pt.to_dict()

        yt = self.yt.to_dict()

        sy = self.sy.to_dict()

        lp = self.lp.to_dict()

        accounting_asset = self.accounting_asset.to_dict()

        underlying_asset = self.underlying_asset.to_dict()

        base_pricing_asset = self.base_pricing_asset.to_dict()

        reward_tokens = []
        for reward_tokens_item_data in self.reward_tokens:
            reward_tokens_item = reward_tokens_item_data.to_dict()
            reward_tokens.append(reward_tokens_item)

        input_tokens = []
        for input_tokens_item_data in self.input_tokens:
            input_tokens_item = input_tokens_item_data.to_dict()
            input_tokens.append(input_tokens_item)

        output_tokens = []
        for output_tokens_item_data in self.output_tokens:
            output_tokens_item = output_tokens_item_data.to_dict()
            output_tokens.append(output_tokens_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pt": pt,
                "yt": yt,
                "sy": sy,
                "lp": lp,
                "accountingAsset": accounting_asset,
                "underlyingAsset": underlying_asset,
                "basePricingAsset": base_pricing_asset,
                "rewardTokens": reward_tokens,
                "inputTokens": input_tokens,
                "outputTokens": output_tokens,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_response import AssetResponse

        d = dict(src_dict)
        pt = AssetResponse.from_dict(d.pop("pt"))

        yt = AssetResponse.from_dict(d.pop("yt"))

        sy = AssetResponse.from_dict(d.pop("sy"))

        lp = AssetResponse.from_dict(d.pop("lp"))

        accounting_asset = AssetResponse.from_dict(d.pop("accountingAsset"))

        underlying_asset = AssetResponse.from_dict(d.pop("underlyingAsset"))

        base_pricing_asset = AssetResponse.from_dict(d.pop("basePricingAsset"))

        reward_tokens = []
        _reward_tokens = d.pop("rewardTokens")
        for reward_tokens_item_data in _reward_tokens:
            reward_tokens_item = AssetResponse.from_dict(reward_tokens_item_data)

            reward_tokens.append(reward_tokens_item)

        input_tokens = []
        _input_tokens = d.pop("inputTokens")
        for input_tokens_item_data in _input_tokens:
            input_tokens_item = AssetResponse.from_dict(input_tokens_item_data)

            input_tokens.append(input_tokens_item)

        output_tokens = []
        _output_tokens = d.pop("outputTokens")
        for output_tokens_item_data in _output_tokens:
            output_tokens_item = AssetResponse.from_dict(output_tokens_item_data)

            output_tokens.append(output_tokens_item)

        market_assets_response = cls(
            pt=pt,
            yt=yt,
            sy=sy,
            lp=lp,
            accounting_asset=accounting_asset,
            underlying_asset=underlying_asset,
            base_pricing_asset=base_pricing_asset,
            reward_tokens=reward_tokens,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
        )

        market_assets_response.additional_properties = d
        return market_assets_response

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
