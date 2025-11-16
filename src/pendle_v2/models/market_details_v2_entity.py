from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pt_yt_implied_yield_change_amount_response import PtYtImpliedYieldChangeAmountResponse
    from ..models.yield_range_response import YieldRangeResponse


T = TypeVar("T", bound="MarketDetailsV2Entity")


@_attrs_define
class MarketDetailsV2Entity:
    """
    Attributes:
        liquidity (float): market liquidity in USD, this is the liquidity of PT and SY in the AMM Example: 1234567.89.
        total_tvl (float): market total TVL (including floating PT that are not in the AMM) in USD Example: 1234567.89.
        trading_volume (float): market 24h trading volume in USD Example: 1234567.89.
        underlying_apy (float): APY of the underlying asset Example: 0.01.
        swap_fee_apy (float): swap fee APY for LP holders, without boosting Example: 0.01.
        pendle_apy (float): APY from Pendle rewards Example: 0.456.
        implied_apy (float): implied APY of market Example: 0.123.
        fee_rate (float): market fee rate Example: 0.003.
        yield_range (YieldRangeResponse):
        aggregated_apy (float): APY including yield, swap fee and Pendle rewards without boosting Example: 0.123.
        max_boosted_apy (float): APY when maximum boost is applies Example: 0.123.
        total_pt (float): total PT in the market Example: 1234567.89.
        total_sy (float): total SY in the market Example: 1234567.89.
        total_supply (float): total supply of the LP token Example: 1234567.89.
        total_active_supply (float): total active supply of the LP token, used for calculate boosting Example:
            1234567.89.
        movement_10_percent (Union[Unset, PtYtImpliedYieldChangeAmountResponse]):
    """

    liquidity: float
    total_tvl: float
    trading_volume: float
    underlying_apy: float
    swap_fee_apy: float
    pendle_apy: float
    implied_apy: float
    fee_rate: float
    yield_range: "YieldRangeResponse"
    aggregated_apy: float
    max_boosted_apy: float
    total_pt: float
    total_sy: float
    total_supply: float
    total_active_supply: float
    movement_10_percent: Union[Unset, "PtYtImpliedYieldChangeAmountResponse"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        liquidity = self.liquidity

        total_tvl = self.total_tvl

        trading_volume = self.trading_volume

        underlying_apy = self.underlying_apy

        swap_fee_apy = self.swap_fee_apy

        pendle_apy = self.pendle_apy

        implied_apy = self.implied_apy

        fee_rate = self.fee_rate

        yield_range = self.yield_range.to_dict()

        aggregated_apy = self.aggregated_apy

        max_boosted_apy = self.max_boosted_apy

        total_pt = self.total_pt

        total_sy = self.total_sy

        total_supply = self.total_supply

        total_active_supply = self.total_active_supply

        movement_10_percent: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.movement_10_percent, Unset):
            movement_10_percent = self.movement_10_percent.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "liquidity": liquidity,
                "totalTvl": total_tvl,
                "tradingVolume": trading_volume,
                "underlyingApy": underlying_apy,
                "swapFeeApy": swap_fee_apy,
                "pendleApy": pendle_apy,
                "impliedApy": implied_apy,
                "feeRate": fee_rate,
                "yieldRange": yield_range,
                "aggregatedApy": aggregated_apy,
                "maxBoostedApy": max_boosted_apy,
                "totalPt": total_pt,
                "totalSy": total_sy,
                "totalSupply": total_supply,
                "totalActiveSupply": total_active_supply,
            }
        )
        if movement_10_percent is not UNSET:
            field_dict["movement10Percent"] = movement_10_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pt_yt_implied_yield_change_amount_response import PtYtImpliedYieldChangeAmountResponse
        from ..models.yield_range_response import YieldRangeResponse

        d = dict(src_dict)
        liquidity = d.pop("liquidity")

        total_tvl = d.pop("totalTvl")

        trading_volume = d.pop("tradingVolume")

        underlying_apy = d.pop("underlyingApy")

        swap_fee_apy = d.pop("swapFeeApy")

        pendle_apy = d.pop("pendleApy")

        implied_apy = d.pop("impliedApy")

        fee_rate = d.pop("feeRate")

        yield_range = YieldRangeResponse.from_dict(d.pop("yieldRange"))

        aggregated_apy = d.pop("aggregatedApy")

        max_boosted_apy = d.pop("maxBoostedApy")

        total_pt = d.pop("totalPt")

        total_sy = d.pop("totalSy")

        total_supply = d.pop("totalSupply")

        total_active_supply = d.pop("totalActiveSupply")

        _movement_10_percent = d.pop("movement10Percent", UNSET)
        movement_10_percent: Union[Unset, PtYtImpliedYieldChangeAmountResponse]
        if isinstance(_movement_10_percent, Unset):
            movement_10_percent = UNSET
        else:
            movement_10_percent = PtYtImpliedYieldChangeAmountResponse.from_dict(_movement_10_percent)

        market_details_v2_entity = cls(
            liquidity=liquidity,
            total_tvl=total_tvl,
            trading_volume=trading_volume,
            underlying_apy=underlying_apy,
            swap_fee_apy=swap_fee_apy,
            pendle_apy=pendle_apy,
            implied_apy=implied_apy,
            fee_rate=fee_rate,
            yield_range=yield_range,
            aggregated_apy=aggregated_apy,
            max_boosted_apy=max_boosted_apy,
            total_pt=total_pt,
            total_sy=total_sy,
            total_supply=total_supply,
            total_active_supply=total_active_supply,
            movement_10_percent=movement_10_percent,
        )

        market_details_v2_entity.additional_properties = d
        return market_details_v2_entity

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
