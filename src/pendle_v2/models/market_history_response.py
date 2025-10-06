import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.valuation_response import ValuationResponse


T = TypeVar("T", bound="MarketHistoryResponse")


@_attrs_define
class MarketHistoryResponse:
    """
    Attributes:
        timestamp (datetime.datetime):
        liquidity (ValuationResponse):
        trading_volume (ValuationResponse):
        underlying_interest_apy (float):
        underlying_reward_apy (float):
        underlying_apy (float):
        implied_apy (float):
        yt_floating_apy (float):
        pt_discount (float):
        swap_fee_apy (float):
        pendle_apy (float):
        aggregated_apy (float):
        lp_reward_apy (float):
        voter_apy (float):
        total_pt (float):
        total_sy (float):
        total_lp (float):
        total_active_supply (float):
        total_tvl (Union['ValuationResponse', None, Unset]):
    """

    timestamp: datetime.datetime
    liquidity: "ValuationResponse"
    trading_volume: "ValuationResponse"
    underlying_interest_apy: float
    underlying_reward_apy: float
    underlying_apy: float
    implied_apy: float
    yt_floating_apy: float
    pt_discount: float
    swap_fee_apy: float
    pendle_apy: float
    aggregated_apy: float
    lp_reward_apy: float
    voter_apy: float
    total_pt: float
    total_sy: float
    total_lp: float
    total_active_supply: float
    total_tvl: Union["ValuationResponse", None, Unset] = UNSET
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

        pt_discount = self.pt_discount

        swap_fee_apy = self.swap_fee_apy

        pendle_apy = self.pendle_apy

        aggregated_apy = self.aggregated_apy

        lp_reward_apy = self.lp_reward_apy

        voter_apy = self.voter_apy

        total_pt = self.total_pt

        total_sy = self.total_sy

        total_lp = self.total_lp

        total_active_supply = self.total_active_supply

        total_tvl: Union[None, Unset, dict[str, Any]]
        if isinstance(self.total_tvl, Unset):
            total_tvl = UNSET
        elif isinstance(self.total_tvl, ValuationResponse):
            total_tvl = self.total_tvl.to_dict()
        else:
            total_tvl = self.total_tvl

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
                "ptDiscount": pt_discount,
                "swapFeeApy": swap_fee_apy,
                "pendleApy": pendle_apy,
                "aggregatedApy": aggregated_apy,
                "lpRewardApy": lp_reward_apy,
                "voterApy": voter_apy,
                "totalPt": total_pt,
                "totalSy": total_sy,
                "totalLp": total_lp,
                "totalActiveSupply": total_active_supply,
            }
        )
        if total_tvl is not UNSET:
            field_dict["totalTvl"] = total_tvl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        pt_discount = d.pop("ptDiscount")

        swap_fee_apy = d.pop("swapFeeApy")

        pendle_apy = d.pop("pendleApy")

        aggregated_apy = d.pop("aggregatedApy")

        lp_reward_apy = d.pop("lpRewardApy")

        voter_apy = d.pop("voterApy")

        total_pt = d.pop("totalPt")

        total_sy = d.pop("totalSy")

        total_lp = d.pop("totalLp")

        total_active_supply = d.pop("totalActiveSupply")

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

        market_history_response = cls(
            timestamp=timestamp,
            liquidity=liquidity,
            trading_volume=trading_volume,
            underlying_interest_apy=underlying_interest_apy,
            underlying_reward_apy=underlying_reward_apy,
            underlying_apy=underlying_apy,
            implied_apy=implied_apy,
            yt_floating_apy=yt_floating_apy,
            pt_discount=pt_discount,
            swap_fee_apy=swap_fee_apy,
            pendle_apy=pendle_apy,
            aggregated_apy=aggregated_apy,
            lp_reward_apy=lp_reward_apy,
            voter_apy=voter_apy,
            total_pt=total_pt,
            total_sy=total_sy,
            total_lp=total_lp,
            total_active_supply=total_active_supply,
            total_tvl=total_tvl,
        )

        market_history_response.additional_properties = d
        return market_history_response

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
