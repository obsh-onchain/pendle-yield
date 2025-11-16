import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.pn_l_transaction_entity_action import PnLTransactionEntityAction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_asset_data import PriceAssetData
    from ..models.spend_unit_data import SpendUnitData
    from ..models.valuation_entity import ValuationEntity


T = TypeVar("T", bound="PnLTransactionEntity")


@_attrs_define
class PnLTransactionEntity:
    """
    Attributes:
        chain_id (float):
        market (str):
        user (str):
        timestamp (datetime.datetime):
        action (PnLTransactionEntityAction):
        pt_data (SpendUnitData):
        yt_data (SpendUnitData):
        lp_data (SpendUnitData):
        price_in_asset (PriceAssetData):
        profit (ValuationEntity):
        tx_value_asset (float): Total value of the transaction in asset
        asset_usd (float): Market asset price in USD
        asset_eth (float): Market asset price in ETH
        pt_exchange_rate (float): PT exchange rate at the time of the transaction
        effective_pt_exchange_rate (Union[Unset, float]): Effective PT exchange rate of this transaction
        pt_exchange_rate_after (Union[Unset, float]): PT exchange rate of market after the transaction
        tx_hash (Union[Unset, str]): Transaction hash, some event does not have this field, example: merkle reward
            distribution
    """

    chain_id: float
    market: str
    user: str
    timestamp: datetime.datetime
    action: PnLTransactionEntityAction
    pt_data: "SpendUnitData"
    yt_data: "SpendUnitData"
    lp_data: "SpendUnitData"
    price_in_asset: "PriceAssetData"
    profit: "ValuationEntity"
    tx_value_asset: float
    asset_usd: float
    asset_eth: float
    pt_exchange_rate: float
    effective_pt_exchange_rate: Union[Unset, float] = UNSET
    pt_exchange_rate_after: Union[Unset, float] = UNSET
    tx_hash: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chain_id = self.chain_id

        market = self.market

        user = self.user

        timestamp = self.timestamp.isoformat()

        action = self.action.value

        pt_data = self.pt_data.to_dict()

        yt_data = self.yt_data.to_dict()

        lp_data = self.lp_data.to_dict()

        price_in_asset = self.price_in_asset.to_dict()

        profit = self.profit.to_dict()

        tx_value_asset = self.tx_value_asset

        asset_usd = self.asset_usd

        asset_eth = self.asset_eth

        pt_exchange_rate = self.pt_exchange_rate

        effective_pt_exchange_rate = self.effective_pt_exchange_rate

        pt_exchange_rate_after = self.pt_exchange_rate_after

        tx_hash = self.tx_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chainId": chain_id,
                "market": market,
                "user": user,
                "timestamp": timestamp,
                "action": action,
                "ptData": pt_data,
                "ytData": yt_data,
                "lpData": lp_data,
                "priceInAsset": price_in_asset,
                "profit": profit,
                "txValueAsset": tx_value_asset,
                "assetUsd": asset_usd,
                "assetEth": asset_eth,
                "ptExchangeRate": pt_exchange_rate,
            }
        )
        if effective_pt_exchange_rate is not UNSET:
            field_dict["effectivePtExchangeRate"] = effective_pt_exchange_rate
        if pt_exchange_rate_after is not UNSET:
            field_dict["ptExchangeRateAfter"] = pt_exchange_rate_after
        if tx_hash is not UNSET:
            field_dict["txHash"] = tx_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.price_asset_data import PriceAssetData
        from ..models.spend_unit_data import SpendUnitData
        from ..models.valuation_entity import ValuationEntity

        d = dict(src_dict)
        chain_id = d.pop("chainId")

        market = d.pop("market")

        user = d.pop("user")

        timestamp = isoparse(d.pop("timestamp"))

        action = PnLTransactionEntityAction(d.pop("action"))

        pt_data = SpendUnitData.from_dict(d.pop("ptData"))

        yt_data = SpendUnitData.from_dict(d.pop("ytData"))

        lp_data = SpendUnitData.from_dict(d.pop("lpData"))

        price_in_asset = PriceAssetData.from_dict(d.pop("priceInAsset"))

        profit = ValuationEntity.from_dict(d.pop("profit"))

        tx_value_asset = d.pop("txValueAsset")

        asset_usd = d.pop("assetUsd")

        asset_eth = d.pop("assetEth")

        pt_exchange_rate = d.pop("ptExchangeRate")

        effective_pt_exchange_rate = d.pop("effectivePtExchangeRate", UNSET)

        pt_exchange_rate_after = d.pop("ptExchangeRateAfter", UNSET)

        tx_hash = d.pop("txHash", UNSET)

        pn_l_transaction_entity = cls(
            chain_id=chain_id,
            market=market,
            user=user,
            timestamp=timestamp,
            action=action,
            pt_data=pt_data,
            yt_data=yt_data,
            lp_data=lp_data,
            price_in_asset=price_in_asset,
            profit=profit,
            tx_value_asset=tx_value_asset,
            asset_usd=asset_usd,
            asset_eth=asset_eth,
            pt_exchange_rate=pt_exchange_rate,
            effective_pt_exchange_rate=effective_pt_exchange_rate,
            pt_exchange_rate_after=pt_exchange_rate_after,
            tx_hash=tx_hash,
        )

        pn_l_transaction_entity.additional_properties = d
        return pn_l_transaction_entity

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
