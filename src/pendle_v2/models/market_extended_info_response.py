from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pt_yt_implied_yield_change_amount_response import PtYtImpliedYieldChangeAmountResponse
    from ..models.yield_range_response import YieldRangeResponse


T = TypeVar("T", bound="MarketExtendedInfoResponse")


@_attrs_define
class MarketExtendedInfoResponse:
    """
    Attributes:
        floating_pt (float):
        floating_sy (float):
        py_unit (str):
        pt_equals_py_unit (bool):
        movement_10_percent (PtYtImpliedYieldChangeAmountResponse):
        sy_supply_cap (Union[None, Unset, float]): Sy supply cap. Only available for sy with cap, otherwise null. Number
            is in decimal format
        sy_current_supply (Union[None, Unset, float]): Sy current supply. Only available for sy with cap, otherwise
            null. Number is in decimal format
        underlying_asset_worth_more (Union[Unset, str]):
        native_withdrawal_url (Union[Unset, str]):
        native_deposit_url (Union[Unset, str]):
        default_migrate_pool (Union[Unset, str]):
        fee_rate (Union[Unset, float]):
        yield_range (Union[Unset, YieldRangeResponse]):
    """

    floating_pt: float
    floating_sy: float
    py_unit: str
    pt_equals_py_unit: bool
    movement_10_percent: "PtYtImpliedYieldChangeAmountResponse"
    sy_supply_cap: Union[None, Unset, float] = UNSET
    sy_current_supply: Union[None, Unset, float] = UNSET
    underlying_asset_worth_more: Union[Unset, str] = UNSET
    native_withdrawal_url: Union[Unset, str] = UNSET
    native_deposit_url: Union[Unset, str] = UNSET
    default_migrate_pool: Union[Unset, str] = UNSET
    fee_rate: Union[Unset, float] = UNSET
    yield_range: Union[Unset, "YieldRangeResponse"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        floating_pt = self.floating_pt

        floating_sy = self.floating_sy

        py_unit = self.py_unit

        pt_equals_py_unit = self.pt_equals_py_unit

        movement_10_percent = self.movement_10_percent.to_dict()

        sy_supply_cap: Union[None, Unset, float]
        if isinstance(self.sy_supply_cap, Unset):
            sy_supply_cap = UNSET
        else:
            sy_supply_cap = self.sy_supply_cap

        sy_current_supply: Union[None, Unset, float]
        if isinstance(self.sy_current_supply, Unset):
            sy_current_supply = UNSET
        else:
            sy_current_supply = self.sy_current_supply

        underlying_asset_worth_more = self.underlying_asset_worth_more

        native_withdrawal_url = self.native_withdrawal_url

        native_deposit_url = self.native_deposit_url

        default_migrate_pool = self.default_migrate_pool

        fee_rate = self.fee_rate

        yield_range: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.yield_range, Unset):
            yield_range = self.yield_range.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "floatingPt": floating_pt,
                "floatingSy": floating_sy,
                "pyUnit": py_unit,
                "ptEqualsPyUnit": pt_equals_py_unit,
                "movement10Percent": movement_10_percent,
            }
        )
        if sy_supply_cap is not UNSET:
            field_dict["sySupplyCap"] = sy_supply_cap
        if sy_current_supply is not UNSET:
            field_dict["syCurrentSupply"] = sy_current_supply
        if underlying_asset_worth_more is not UNSET:
            field_dict["underlyingAssetWorthMore"] = underlying_asset_worth_more
        if native_withdrawal_url is not UNSET:
            field_dict["nativeWithdrawalURL"] = native_withdrawal_url
        if native_deposit_url is not UNSET:
            field_dict["nativeDepositURL"] = native_deposit_url
        if default_migrate_pool is not UNSET:
            field_dict["defaultMigratePool"] = default_migrate_pool
        if fee_rate is not UNSET:
            field_dict["feeRate"] = fee_rate
        if yield_range is not UNSET:
            field_dict["yieldRange"] = yield_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pt_yt_implied_yield_change_amount_response import PtYtImpliedYieldChangeAmountResponse
        from ..models.yield_range_response import YieldRangeResponse

        d = dict(src_dict)
        floating_pt = d.pop("floatingPt")

        floating_sy = d.pop("floatingSy")

        py_unit = d.pop("pyUnit")

        pt_equals_py_unit = d.pop("ptEqualsPyUnit")

        movement_10_percent = PtYtImpliedYieldChangeAmountResponse.from_dict(d.pop("movement10Percent"))

        def _parse_sy_supply_cap(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        sy_supply_cap = _parse_sy_supply_cap(d.pop("sySupplyCap", UNSET))

        def _parse_sy_current_supply(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        sy_current_supply = _parse_sy_current_supply(d.pop("syCurrentSupply", UNSET))

        underlying_asset_worth_more = d.pop("underlyingAssetWorthMore", UNSET)

        native_withdrawal_url = d.pop("nativeWithdrawalURL", UNSET)

        native_deposit_url = d.pop("nativeDepositURL", UNSET)

        default_migrate_pool = d.pop("defaultMigratePool", UNSET)

        fee_rate = d.pop("feeRate", UNSET)

        _yield_range = d.pop("yieldRange", UNSET)
        yield_range: Union[Unset, YieldRangeResponse]
        if isinstance(_yield_range, Unset):
            yield_range = UNSET
        else:
            yield_range = YieldRangeResponse.from_dict(_yield_range)

        market_extended_info_response = cls(
            floating_pt=floating_pt,
            floating_sy=floating_sy,
            py_unit=py_unit,
            pt_equals_py_unit=pt_equals_py_unit,
            movement_10_percent=movement_10_percent,
            sy_supply_cap=sy_supply_cap,
            sy_current_supply=sy_current_supply,
            underlying_asset_worth_more=underlying_asset_worth_more,
            native_withdrawal_url=native_withdrawal_url,
            native_deposit_url=native_deposit_url,
            default_migrate_pool=default_migrate_pool,
            fee_rate=fee_rate,
            yield_range=yield_range,
        )

        market_extended_info_response.additional_properties = d
        return market_extended_info_response

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
