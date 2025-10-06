from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pt_yt_implied_yield_change_amount_response import PtYtImpliedYieldChangeAmountResponse
    from ..models.yield_range_response import YieldRangeResponse


T = TypeVar("T", bound="MarketDetails")


@_attrs_define
class MarketDetails:
    """
    Attributes:
        liquidity (float): market liquidity in USD Example: 1234567.89.
        pendle_apy (float): APY from Pendle rewards Example: 0.456.
        implied_apy (float): implied APY of market Example: 0.123.
        fee_rate (float): market fee rate Example: 0.003.
        yield_range (YieldRangeResponse):
        aggregated_apy (float): APY including yield, swap fee and Pendle rewards without boosting Example: 0.123.
        max_boosted_apy (float): APY when maximum boost is applies Example: 0.123.
        movement_10_percent (Union[Unset, PtYtImpliedYieldChangeAmountResponse]):
    """

    liquidity: float
    pendle_apy: float
    implied_apy: float
    fee_rate: float
    yield_range: "YieldRangeResponse"
    aggregated_apy: float
    max_boosted_apy: float
    movement_10_percent: Union[Unset, "PtYtImpliedYieldChangeAmountResponse"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        liquidity = self.liquidity

        pendle_apy = self.pendle_apy

        implied_apy = self.implied_apy

        fee_rate = self.fee_rate

        yield_range = self.yield_range.to_dict()

        aggregated_apy = self.aggregated_apy

        max_boosted_apy = self.max_boosted_apy

        movement_10_percent: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.movement_10_percent, Unset):
            movement_10_percent = self.movement_10_percent.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "liquidity": liquidity,
                "pendleApy": pendle_apy,
                "impliedApy": implied_apy,
                "feeRate": fee_rate,
                "yieldRange": yield_range,
                "aggregatedApy": aggregated_apy,
                "maxBoostedApy": max_boosted_apy,
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

        pendle_apy = d.pop("pendleApy")

        implied_apy = d.pop("impliedApy")

        fee_rate = d.pop("feeRate")

        yield_range = YieldRangeResponse.from_dict(d.pop("yieldRange"))

        aggregated_apy = d.pop("aggregatedApy")

        max_boosted_apy = d.pop("maxBoostedApy")

        _movement_10_percent = d.pop("movement10Percent", UNSET)
        movement_10_percent: Union[Unset, PtYtImpliedYieldChangeAmountResponse]
        if isinstance(_movement_10_percent, Unset):
            movement_10_percent = UNSET
        else:
            movement_10_percent = PtYtImpliedYieldChangeAmountResponse.from_dict(_movement_10_percent)

        market_details = cls(
            liquidity=liquidity,
            pendle_apy=pendle_apy,
            implied_apy=implied_apy,
            fee_rate=fee_rate,
            yield_range=yield_range,
            aggregated_apy=aggregated_apy,
            max_boosted_apy=max_boosted_apy,
            movement_10_percent=movement_10_percent,
        )

        market_details.additional_properties = d
        return market_details

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
