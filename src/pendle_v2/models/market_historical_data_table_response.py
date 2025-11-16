from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketHistoricalDataTableResponse")


@_attrs_define
class MarketHistoricalDataTableResponse:
    """
    Attributes:
        total (float):
        timestamp_start (float):
        timestamp_end (float):
        timestamp (list[float]): Array of timestamp in second
        max_apy (Union[Unset, list[float]]): Array of maxApy. 0.5 means 50%
        base_apy (Union[Unset, list[float]]): Array of baseApy. 0.5 means 50%
        underlying_apy (Union[Unset, list[float]]): Array of underlyingApy. 0.5 means 50%
        implied_apy (Union[Unset, list[float]]): Array of impliedApy. 0.5 means 50%
        tvl (Union[Unset, list[float]]): Array of tvl (market liquidity in USD)
        total_tvl (Union[Unset, list[float]]): Array of total TVL (in USD)
        underlying_interest_apy (Union[Unset, list[float]]): Array of underlying interest APY. 0.5 means 50%
        underlying_reward_apy (Union[Unset, list[float]]): Array of underlying reward APY. 0.5 means 50%
        yt_floating_apy (Union[Unset, list[float]]): Array of YT floating APY. 0.5 means 50%
        swap_fee_apy (Union[Unset, list[float]]): Array of swap fee APY. 0.5 means 50%
        voter_apr (Union[Unset, list[float]]): Array of voter APR. 0.5 means 50%
        pendle_apy (Union[Unset, list[float]]): Array of PENDLE APY. 0.5 means 50%
        lp_reward_apy (Union[Unset, list[float]]): Array of LP reward APY. 0.5 means 50%
        total_pt (Union[Unset, list[float]]): Array of total PT amount
        total_sy (Union[Unset, list[float]]): Array of total SY amount
        total_supply (Union[Unset, list[float]]): Array of total LP supply
        pt_price (Union[Unset, list[float]]): Array of PT price (in USD)
        yt_price (Union[Unset, list[float]]): Array of YT price (in USD)
        sy_price (Union[Unset, list[float]]): Array of SY price (in USD)
        lp_price (Union[Unset, list[float]]): Array of LP price (in USD)
        last_epoch_votes (Union[Unset, list[float]]): Array of last epoch votes
        explicit_swap_fee (Union[Unset, list[float]]): Array of explicit swap fee (in USD). Only available for daily and
            weekly timeframes
        implicit_swap_fee (Union[Unset, list[float]]): Array of implicit swap fee (in USD). Only available for daily and
            weekly timeframes
        limit_order_fee (Union[Unset, list[float]]): Array of limit order fee (in USD). Only available for daily and
            weekly timeframes
    """

    total: float
    timestamp_start: float
    timestamp_end: float
    timestamp: list[float]
    max_apy: Union[Unset, list[float]] = UNSET
    base_apy: Union[Unset, list[float]] = UNSET
    underlying_apy: Union[Unset, list[float]] = UNSET
    implied_apy: Union[Unset, list[float]] = UNSET
    tvl: Union[Unset, list[float]] = UNSET
    total_tvl: Union[Unset, list[float]] = UNSET
    underlying_interest_apy: Union[Unset, list[float]] = UNSET
    underlying_reward_apy: Union[Unset, list[float]] = UNSET
    yt_floating_apy: Union[Unset, list[float]] = UNSET
    swap_fee_apy: Union[Unset, list[float]] = UNSET
    voter_apr: Union[Unset, list[float]] = UNSET
    pendle_apy: Union[Unset, list[float]] = UNSET
    lp_reward_apy: Union[Unset, list[float]] = UNSET
    total_pt: Union[Unset, list[float]] = UNSET
    total_sy: Union[Unset, list[float]] = UNSET
    total_supply: Union[Unset, list[float]] = UNSET
    pt_price: Union[Unset, list[float]] = UNSET
    yt_price: Union[Unset, list[float]] = UNSET
    sy_price: Union[Unset, list[float]] = UNSET
    lp_price: Union[Unset, list[float]] = UNSET
    last_epoch_votes: Union[Unset, list[float]] = UNSET
    explicit_swap_fee: Union[Unset, list[float]] = UNSET
    implicit_swap_fee: Union[Unset, list[float]] = UNSET
    limit_order_fee: Union[Unset, list[float]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        timestamp_start = self.timestamp_start

        timestamp_end = self.timestamp_end

        timestamp = self.timestamp

        max_apy: Union[Unset, list[float]] = UNSET
        if not isinstance(self.max_apy, Unset):
            max_apy = self.max_apy

        base_apy: Union[Unset, list[float]] = UNSET
        if not isinstance(self.base_apy, Unset):
            base_apy = self.base_apy

        underlying_apy: Union[Unset, list[float]] = UNSET
        if not isinstance(self.underlying_apy, Unset):
            underlying_apy = self.underlying_apy

        implied_apy: Union[Unset, list[float]] = UNSET
        if not isinstance(self.implied_apy, Unset):
            implied_apy = self.implied_apy

        tvl: Union[Unset, list[float]] = UNSET
        if not isinstance(self.tvl, Unset):
            tvl = self.tvl

        total_tvl: Union[Unset, list[float]] = UNSET
        if not isinstance(self.total_tvl, Unset):
            total_tvl = self.total_tvl

        underlying_interest_apy: Union[Unset, list[float]] = UNSET
        if not isinstance(self.underlying_interest_apy, Unset):
            underlying_interest_apy = self.underlying_interest_apy

        underlying_reward_apy: Union[Unset, list[float]] = UNSET
        if not isinstance(self.underlying_reward_apy, Unset):
            underlying_reward_apy = self.underlying_reward_apy

        yt_floating_apy: Union[Unset, list[float]] = UNSET
        if not isinstance(self.yt_floating_apy, Unset):
            yt_floating_apy = self.yt_floating_apy

        swap_fee_apy: Union[Unset, list[float]] = UNSET
        if not isinstance(self.swap_fee_apy, Unset):
            swap_fee_apy = self.swap_fee_apy

        voter_apr: Union[Unset, list[float]] = UNSET
        if not isinstance(self.voter_apr, Unset):
            voter_apr = self.voter_apr

        pendle_apy: Union[Unset, list[float]] = UNSET
        if not isinstance(self.pendle_apy, Unset):
            pendle_apy = self.pendle_apy

        lp_reward_apy: Union[Unset, list[float]] = UNSET
        if not isinstance(self.lp_reward_apy, Unset):
            lp_reward_apy = self.lp_reward_apy

        total_pt: Union[Unset, list[float]] = UNSET
        if not isinstance(self.total_pt, Unset):
            total_pt = self.total_pt

        total_sy: Union[Unset, list[float]] = UNSET
        if not isinstance(self.total_sy, Unset):
            total_sy = self.total_sy

        total_supply: Union[Unset, list[float]] = UNSET
        if not isinstance(self.total_supply, Unset):
            total_supply = self.total_supply

        pt_price: Union[Unset, list[float]] = UNSET
        if not isinstance(self.pt_price, Unset):
            pt_price = self.pt_price

        yt_price: Union[Unset, list[float]] = UNSET
        if not isinstance(self.yt_price, Unset):
            yt_price = self.yt_price

        sy_price: Union[Unset, list[float]] = UNSET
        if not isinstance(self.sy_price, Unset):
            sy_price = self.sy_price

        lp_price: Union[Unset, list[float]] = UNSET
        if not isinstance(self.lp_price, Unset):
            lp_price = self.lp_price

        last_epoch_votes: Union[Unset, list[float]] = UNSET
        if not isinstance(self.last_epoch_votes, Unset):
            last_epoch_votes = self.last_epoch_votes

        explicit_swap_fee: Union[Unset, list[float]] = UNSET
        if not isinstance(self.explicit_swap_fee, Unset):
            explicit_swap_fee = self.explicit_swap_fee

        implicit_swap_fee: Union[Unset, list[float]] = UNSET
        if not isinstance(self.implicit_swap_fee, Unset):
            implicit_swap_fee = self.implicit_swap_fee

        limit_order_fee: Union[Unset, list[float]] = UNSET
        if not isinstance(self.limit_order_fee, Unset):
            limit_order_fee = self.limit_order_fee

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "timestamp_start": timestamp_start,
                "timestamp_end": timestamp_end,
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
        total = d.pop("total")

        timestamp_start = d.pop("timestamp_start")

        timestamp_end = d.pop("timestamp_end")

        timestamp = cast(list[float], d.pop("timestamp"))

        max_apy = cast(list[float], d.pop("maxApy", UNSET))

        base_apy = cast(list[float], d.pop("baseApy", UNSET))

        underlying_apy = cast(list[float], d.pop("underlyingApy", UNSET))

        implied_apy = cast(list[float], d.pop("impliedApy", UNSET))

        tvl = cast(list[float], d.pop("tvl", UNSET))

        total_tvl = cast(list[float], d.pop("totalTvl", UNSET))

        underlying_interest_apy = cast(list[float], d.pop("underlyingInterestApy", UNSET))

        underlying_reward_apy = cast(list[float], d.pop("underlyingRewardApy", UNSET))

        yt_floating_apy = cast(list[float], d.pop("ytFloatingApy", UNSET))

        swap_fee_apy = cast(list[float], d.pop("swapFeeApy", UNSET))

        voter_apr = cast(list[float], d.pop("voterApr", UNSET))

        pendle_apy = cast(list[float], d.pop("pendleApy", UNSET))

        lp_reward_apy = cast(list[float], d.pop("lpRewardApy", UNSET))

        total_pt = cast(list[float], d.pop("totalPt", UNSET))

        total_sy = cast(list[float], d.pop("totalSy", UNSET))

        total_supply = cast(list[float], d.pop("totalSupply", UNSET))

        pt_price = cast(list[float], d.pop("ptPrice", UNSET))

        yt_price = cast(list[float], d.pop("ytPrice", UNSET))

        sy_price = cast(list[float], d.pop("syPrice", UNSET))

        lp_price = cast(list[float], d.pop("lpPrice", UNSET))

        last_epoch_votes = cast(list[float], d.pop("lastEpochVotes", UNSET))

        explicit_swap_fee = cast(list[float], d.pop("explicitSwapFee", UNSET))

        implicit_swap_fee = cast(list[float], d.pop("implicitSwapFee", UNSET))

        limit_order_fee = cast(list[float], d.pop("limitOrderFee", UNSET))

        market_historical_data_table_response = cls(
            total=total,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end,
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
            explicit_swap_fee=explicit_swap_fee,
            implicit_swap_fee=implicit_swap_fee,
            limit_order_fee=limit_order_fee,
        )

        market_historical_data_table_response.additional_properties = d
        return market_historical_data_table_response

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
