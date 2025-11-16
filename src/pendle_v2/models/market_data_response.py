import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.estimated_daily_pool_reward_response import EstimatedDailyPoolRewardResponse
    from ..models.valuation_response import ValuationResponse


T = TypeVar("T", bound="MarketDataResponse")


@_attrs_define
class MarketDataResponse:
    """
    Attributes:
        timestamp (datetime.datetime): Timestamp of the market data snapshot
        liquidity (ValuationResponse):
        trading_volume (ValuationResponse):
        underlying_interest_apy (float): Annual percentage yield from the underlying asset interest
        underlying_reward_apy (float): Annual percentage yield from the underlying asset rewards
        underlying_apy (float): APY of the underlying asset
        implied_apy (float): Implied APY of market
        yt_floating_apy (float): Floating APY for YT holders (underlyingApy - impliedApy)
        swap_fee_apy (float): Swap fee APY for LP holders, without boosting
        voter_apy (float): APY for voters (vePENDLE holders) from voting on this pool
        pt_discount (float): PT discount relative to underlying asset
        pendle_apy (float): APY from Pendle rewards
        lp_reward_apy (float): APY from LP reward tokens
        aggregated_apy (float): APY including yield, swap fee and Pendle rewards without boosting
        max_boosted_apy (float): APY when maximum boost is applied
        estimated_daily_pool_rewards (list['EstimatedDailyPoolRewardResponse']): Estimated daily pool rewards broken
            down by asset
        total_pt (float): Total PT in the market
        total_sy (float): Total SY in the market
        total_lp (float): Total supply of the LP token
        total_active_supply (float): Total active supply of the LP token, used for calculate boosting
        asset_price_usd (float): Price of the accounting asset in USD
        total_tvl (Union['ValuationResponse', None, Unset]): Market total TVL (including floating PT that are not in the
            AMM)
        arb_apy (Union[Unset, float]): APY from arbitrage opportunities
    """

    timestamp: datetime.datetime
    liquidity: "ValuationResponse"
    trading_volume: "ValuationResponse"
    underlying_interest_apy: float
    underlying_reward_apy: float
    underlying_apy: float
    implied_apy: float
    yt_floating_apy: float
    swap_fee_apy: float
    voter_apy: float
    pt_discount: float
    pendle_apy: float
    lp_reward_apy: float
    aggregated_apy: float
    max_boosted_apy: float
    estimated_daily_pool_rewards: list["EstimatedDailyPoolRewardResponse"]
    total_pt: float
    total_sy: float
    total_lp: float
    total_active_supply: float
    asset_price_usd: float
    total_tvl: Union["ValuationResponse", None, Unset] = UNSET
    arb_apy: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.valuation_response import ValuationResponse

        timestamp = self.timestamp.isoformat()

        liquidity = self.liquidity.to_dict()

        trading_volume = self.trading_volume.to_dict()

        underlying_interest_apy = self.underlying_interest_apy

        underlying_reward_apy = self.underlying_reward_apy

        underlying_apy = self.underlying_apy

        implied_apy = self.implied_apy

        yt_floating_apy = self.yt_floating_apy

        swap_fee_apy = self.swap_fee_apy

        voter_apy = self.voter_apy

        pt_discount = self.pt_discount

        pendle_apy = self.pendle_apy

        lp_reward_apy = self.lp_reward_apy

        aggregated_apy = self.aggregated_apy

        max_boosted_apy = self.max_boosted_apy

        estimated_daily_pool_rewards = []
        for estimated_daily_pool_rewards_item_data in self.estimated_daily_pool_rewards:
            estimated_daily_pool_rewards_item = estimated_daily_pool_rewards_item_data.to_dict()
            estimated_daily_pool_rewards.append(estimated_daily_pool_rewards_item)

        total_pt = self.total_pt

        total_sy = self.total_sy

        total_lp = self.total_lp

        total_active_supply = self.total_active_supply

        asset_price_usd = self.asset_price_usd

        total_tvl: Union[None, Unset, dict[str, Any]]
        if isinstance(self.total_tvl, Unset):
            total_tvl = UNSET
        elif isinstance(self.total_tvl, ValuationResponse):
            total_tvl = self.total_tvl.to_dict()
        else:
            total_tvl = self.total_tvl

        arb_apy = self.arb_apy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "liquidity": liquidity,
                "tradingVolume": trading_volume,
                "underlyingInterestApy": underlying_interest_apy,
                "underlyingRewardApy": underlying_reward_apy,
                "underlyingApy": underlying_apy,
                "impliedApy": implied_apy,
                "ytFloatingApy": yt_floating_apy,
                "swapFeeApy": swap_fee_apy,
                "voterApy": voter_apy,
                "ptDiscount": pt_discount,
                "pendleApy": pendle_apy,
                "lpRewardApy": lp_reward_apy,
                "aggregatedApy": aggregated_apy,
                "maxBoostedApy": max_boosted_apy,
                "estimatedDailyPoolRewards": estimated_daily_pool_rewards,
                "totalPt": total_pt,
                "totalSy": total_sy,
                "totalLp": total_lp,
                "totalActiveSupply": total_active_supply,
                "assetPriceUsd": asset_price_usd,
            }
        )
        if total_tvl is not UNSET:
            field_dict["totalTvl"] = total_tvl
        if arb_apy is not UNSET:
            field_dict["arbApy"] = arb_apy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.estimated_daily_pool_reward_response import EstimatedDailyPoolRewardResponse
        from ..models.valuation_response import ValuationResponse

        d = dict(src_dict)
        timestamp = isoparse(d.pop("timestamp"))

        liquidity = ValuationResponse.from_dict(d.pop("liquidity"))

        trading_volume = ValuationResponse.from_dict(d.pop("tradingVolume"))

        underlying_interest_apy = d.pop("underlyingInterestApy")

        underlying_reward_apy = d.pop("underlyingRewardApy")

        underlying_apy = d.pop("underlyingApy")

        implied_apy = d.pop("impliedApy")

        yt_floating_apy = d.pop("ytFloatingApy")

        swap_fee_apy = d.pop("swapFeeApy")

        voter_apy = d.pop("voterApy")

        pt_discount = d.pop("ptDiscount")

        pendle_apy = d.pop("pendleApy")

        lp_reward_apy = d.pop("lpRewardApy")

        aggregated_apy = d.pop("aggregatedApy")

        max_boosted_apy = d.pop("maxBoostedApy")

        estimated_daily_pool_rewards = []
        _estimated_daily_pool_rewards = d.pop("estimatedDailyPoolRewards")
        for estimated_daily_pool_rewards_item_data in _estimated_daily_pool_rewards:
            estimated_daily_pool_rewards_item = EstimatedDailyPoolRewardResponse.from_dict(
                estimated_daily_pool_rewards_item_data
            )

            estimated_daily_pool_rewards.append(estimated_daily_pool_rewards_item)

        total_pt = d.pop("totalPt")

        total_sy = d.pop("totalSy")

        total_lp = d.pop("totalLp")

        total_active_supply = d.pop("totalActiveSupply")

        asset_price_usd = d.pop("assetPriceUsd")

        def _parse_total_tvl(data: object) -> Union["ValuationResponse", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                total_tvl_type_1 = ValuationResponse.from_dict(data)

                return total_tvl_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ValuationResponse", None, Unset], data)

        total_tvl = _parse_total_tvl(d.pop("totalTvl", UNSET))

        arb_apy = d.pop("arbApy", UNSET)

        market_data_response = cls(
            timestamp=timestamp,
            liquidity=liquidity,
            trading_volume=trading_volume,
            underlying_interest_apy=underlying_interest_apy,
            underlying_reward_apy=underlying_reward_apy,
            underlying_apy=underlying_apy,
            implied_apy=implied_apy,
            yt_floating_apy=yt_floating_apy,
            swap_fee_apy=swap_fee_apy,
            voter_apy=voter_apy,
            pt_discount=pt_discount,
            pendle_apy=pendle_apy,
            lp_reward_apy=lp_reward_apy,
            aggregated_apy=aggregated_apy,
            max_boosted_apy=max_boosted_apy,
            estimated_daily_pool_rewards=estimated_daily_pool_rewards,
            total_pt=total_pt,
            total_sy=total_sy,
            total_lp=total_lp,
            total_active_supply=total_active_supply,
            asset_price_usd=asset_price_usd,
            total_tvl=total_tvl,
            arb_apy=arb_apy,
        )

        market_data_response.additional_properties = d
        return market_data_response

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
