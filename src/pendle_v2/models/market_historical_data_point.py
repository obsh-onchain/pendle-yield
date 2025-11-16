import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketHistoricalDataPoint")


@_attrs_define
class MarketHistoricalDataPoint:
    """
    Attributes:
        timestamp (datetime.datetime): Timestamp in ISO format
        max_apy (Union[Unset, float]): APY when maximum boost is applied
        base_apy (Union[Unset, float]): APY including yield, swap fee and Pendle rewards without boosting
        underlying_apy (Union[Unset, float]): APY of the underlying asset
        implied_apy (Union[Unset, float]): Implied APY of market
        tvl (Union[Unset, float]): Market liquidity (TVL in the pool) in USD
        total_tvl (Union[Unset, float]): Market total TVL (including floating PT that are not in the AMM) in USD
        underlying_interest_apy (Union[Unset, float]): Annual percentage yield from the underlying asset interest
        underlying_reward_apy (Union[Unset, float]): Annual percentage yield from the underlying asset rewards
        yt_floating_apy (Union[Unset, float]): Floating APY for YT holders (underlyingApy - impliedApy)
        swap_fee_apy (Union[Unset, float]): Swap fee APY for LP holders, without boosting
        voter_apr (Union[Unset, float]): APY for voters (vePENDLE holders) from voting on this pool
        pendle_apy (Union[Unset, float]): APY from Pendle rewards
        lp_reward_apy (Union[Unset, float]): APY from LP reward tokens
        total_pt (Union[Unset, float]): Total PT in the market
        total_sy (Union[Unset, float]): Total SY in the market
        total_supply (Union[Unset, float]): Total supply of the LP token
        pt_price (Union[Unset, float]): PT price in USD
        yt_price (Union[Unset, float]): YT price in USD
        sy_price (Union[Unset, float]): SY price in USD
        lp_price (Union[Unset, float]): LP price in USD
        last_epoch_votes (Union[Unset, float]): Last epoch votes
        trading_volume (Union[Unset, float]): 24h trading volume in USD
        explicit_swap_fee (Union[Unset, float]): Explicit swap fee in USD (only available for daily and weekly
            timeframes)
        implicit_swap_fee (Union[Unset, float]): Implicit swap fee in USD (only available for daily and weekly
            timeframes)
        limit_order_fee (Union[Unset, float]): Limit order fee in USD (only available for daily and weekly timeframes)
    """

    timestamp: datetime.datetime
    max_apy: Union[Unset, float] = UNSET
    base_apy: Union[Unset, float] = UNSET
    underlying_apy: Union[Unset, float] = UNSET
    implied_apy: Union[Unset, float] = UNSET
    tvl: Union[Unset, float] = UNSET
    total_tvl: Union[Unset, float] = UNSET
    underlying_interest_apy: Union[Unset, float] = UNSET
    underlying_reward_apy: Union[Unset, float] = UNSET
    yt_floating_apy: Union[Unset, float] = UNSET
    swap_fee_apy: Union[Unset, float] = UNSET
    voter_apr: Union[Unset, float] = UNSET
    pendle_apy: Union[Unset, float] = UNSET
    lp_reward_apy: Union[Unset, float] = UNSET
    total_pt: Union[Unset, float] = UNSET
    total_sy: Union[Unset, float] = UNSET
    total_supply: Union[Unset, float] = UNSET
    pt_price: Union[Unset, float] = UNSET
    yt_price: Union[Unset, float] = UNSET
    sy_price: Union[Unset, float] = UNSET
    lp_price: Union[Unset, float] = UNSET
    last_epoch_votes: Union[Unset, float] = UNSET
    trading_volume: Union[Unset, float] = UNSET
    explicit_swap_fee: Union[Unset, float] = UNSET
    implicit_swap_fee: Union[Unset, float] = UNSET
    limit_order_fee: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        max_apy = self.max_apy

        base_apy = self.base_apy

        underlying_apy = self.underlying_apy

        implied_apy = self.implied_apy

        tvl = self.tvl

        total_tvl = self.total_tvl

        underlying_interest_apy = self.underlying_interest_apy

        underlying_reward_apy = self.underlying_reward_apy

        yt_floating_apy = self.yt_floating_apy

        swap_fee_apy = self.swap_fee_apy

        voter_apr = self.voter_apr

        pendle_apy = self.pendle_apy

        lp_reward_apy = self.lp_reward_apy

        total_pt = self.total_pt

        total_sy = self.total_sy

        total_supply = self.total_supply

        pt_price = self.pt_price

        yt_price = self.yt_price

        sy_price = self.sy_price

        lp_price = self.lp_price

        last_epoch_votes = self.last_epoch_votes

        trading_volume = self.trading_volume

        explicit_swap_fee = self.explicit_swap_fee

        implicit_swap_fee = self.implicit_swap_fee

        limit_order_fee = self.limit_order_fee

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
            }
        )
        if max_apy is not UNSET:
            field_dict["maxApy"] = max_apy
        if base_apy is not UNSET:
            field_dict["baseApy"] = base_apy
        if underlying_apy is not UNSET:
            field_dict["underlyingApy"] = underlying_apy
        if implied_apy is not UNSET:
            field_dict["impliedApy"] = implied_apy
        if tvl is not UNSET:
            field_dict["tvl"] = tvl
        if total_tvl is not UNSET:
            field_dict["totalTvl"] = total_tvl
        if underlying_interest_apy is not UNSET:
            field_dict["underlyingInterestApy"] = underlying_interest_apy
        if underlying_reward_apy is not UNSET:
            field_dict["underlyingRewardApy"] = underlying_reward_apy
        if yt_floating_apy is not UNSET:
            field_dict["ytFloatingApy"] = yt_floating_apy
        if swap_fee_apy is not UNSET:
            field_dict["swapFeeApy"] = swap_fee_apy
        if voter_apr is not UNSET:
            field_dict["voterApr"] = voter_apr
        if pendle_apy is not UNSET:
            field_dict["pendleApy"] = pendle_apy
        if lp_reward_apy is not UNSET:
            field_dict["lpRewardApy"] = lp_reward_apy
        if total_pt is not UNSET:
            field_dict["totalPt"] = total_pt
        if total_sy is not UNSET:
            field_dict["totalSy"] = total_sy
        if total_supply is not UNSET:
            field_dict["totalSupply"] = total_supply
        if pt_price is not UNSET:
            field_dict["ptPrice"] = pt_price
        if yt_price is not UNSET:
            field_dict["ytPrice"] = yt_price
        if sy_price is not UNSET:
            field_dict["syPrice"] = sy_price
        if lp_price is not UNSET:
            field_dict["lpPrice"] = lp_price
        if last_epoch_votes is not UNSET:
            field_dict["lastEpochVotes"] = last_epoch_votes
        if trading_volume is not UNSET:
            field_dict["tradingVolume"] = trading_volume
        if explicit_swap_fee is not UNSET:
            field_dict["explicitSwapFee"] = explicit_swap_fee
        if implicit_swap_fee is not UNSET:
            field_dict["implicitSwapFee"] = implicit_swap_fee
        if limit_order_fee is not UNSET:
            field_dict["limitOrderFee"] = limit_order_fee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = isoparse(d.pop("timestamp"))

        max_apy = d.pop("maxApy", UNSET)

        base_apy = d.pop("baseApy", UNSET)

        underlying_apy = d.pop("underlyingApy", UNSET)

        implied_apy = d.pop("impliedApy", UNSET)

        tvl = d.pop("tvl", UNSET)

        total_tvl = d.pop("totalTvl", UNSET)

        underlying_interest_apy = d.pop("underlyingInterestApy", UNSET)

        underlying_reward_apy = d.pop("underlyingRewardApy", UNSET)

        yt_floating_apy = d.pop("ytFloatingApy", UNSET)

        swap_fee_apy = d.pop("swapFeeApy", UNSET)

        voter_apr = d.pop("voterApr", UNSET)

        pendle_apy = d.pop("pendleApy", UNSET)

        lp_reward_apy = d.pop("lpRewardApy", UNSET)

        total_pt = d.pop("totalPt", UNSET)

        total_sy = d.pop("totalSy", UNSET)

        total_supply = d.pop("totalSupply", UNSET)

        pt_price = d.pop("ptPrice", UNSET)

        yt_price = d.pop("ytPrice", UNSET)

        sy_price = d.pop("syPrice", UNSET)

        lp_price = d.pop("lpPrice", UNSET)

        last_epoch_votes = d.pop("lastEpochVotes", UNSET)

        trading_volume = d.pop("tradingVolume", UNSET)

        explicit_swap_fee = d.pop("explicitSwapFee", UNSET)

        implicit_swap_fee = d.pop("implicitSwapFee", UNSET)

        limit_order_fee = d.pop("limitOrderFee", UNSET)

        market_historical_data_point = cls(
            timestamp=timestamp,
            max_apy=max_apy,
            base_apy=base_apy,
            underlying_apy=underlying_apy,
            implied_apy=implied_apy,
            tvl=tvl,
            total_tvl=total_tvl,
            underlying_interest_apy=underlying_interest_apy,
            underlying_reward_apy=underlying_reward_apy,
            yt_floating_apy=yt_floating_apy,
            swap_fee_apy=swap_fee_apy,
            voter_apr=voter_apr,
            pendle_apy=pendle_apy,
            lp_reward_apy=lp_reward_apy,
            total_pt=total_pt,
            total_sy=total_sy,
            total_supply=total_supply,
            pt_price=pt_price,
            yt_price=yt_price,
            sy_price=sy_price,
            lp_price=lp_price,
            last_epoch_votes=last_epoch_votes,
            trading_volume=trading_volume,
            explicit_swap_fee=explicit_swap_fee,
            implicit_swap_fee=implicit_swap_fee,
            limit_order_fee=limit_order_fee,
        )

        market_historical_data_point.additional_properties = d
        return market_historical_data_point

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
