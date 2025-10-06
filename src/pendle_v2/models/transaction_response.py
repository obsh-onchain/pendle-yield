import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.asset_amount_response import AssetAmountResponse
    from ..models.market_basic_response import MarketBasicResponse
    from ..models.transaction_response_asset_prices import TransactionResponseAssetPrices
    from ..models.valuation_response import ValuationResponse


T = TypeVar("T", bound="TransactionResponse")


@_attrs_define
class TransactionResponse:
    """
    Attributes:
        id (str):
        chain_id (float):
        tx_hash (str):
        block_number (float):
        timestamp (datetime.datetime):
        action (str):
        origin (str):
        market (MarketBasicResponse):
        inputs (list['AssetAmountResponse']):
        outputs (list['AssetAmountResponse']):
        user (str):
        valuation (ValuationResponse):
        implicit_swap_fee_sy (float):
        explicit_swap_fee_sy (float):
        implied_apy (float):
        asset_prices (TransactionResponseAssetPrices):
        gas_used (float):
    """

    id: str
    chain_id: float
    tx_hash: str
    block_number: float
    timestamp: datetime.datetime
    action: str
    origin: str
    market: "MarketBasicResponse"
    inputs: list["AssetAmountResponse"]
    outputs: list["AssetAmountResponse"]
    user: str
    valuation: "ValuationResponse"
    implicit_swap_fee_sy: float
    explicit_swap_fee_sy: float
    implied_apy: float
    asset_prices: "TransactionResponseAssetPrices"
    gas_used: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        chain_id = self.chain_id

        tx_hash = self.tx_hash

        block_number = self.block_number

        timestamp = self.timestamp.isoformat()

        action = self.action

        origin = self.origin

        market = self.market.to_dict()

        inputs = []
        for inputs_item_data in self.inputs:
            inputs_item = inputs_item_data.to_dict()
            inputs.append(inputs_item)

        outputs = []
        for outputs_item_data in self.outputs:
            outputs_item = outputs_item_data.to_dict()
            outputs.append(outputs_item)

        user = self.user

        valuation = self.valuation.to_dict()

        implicit_swap_fee_sy = self.implicit_swap_fee_sy

        explicit_swap_fee_sy = self.explicit_swap_fee_sy

        implied_apy = self.implied_apy

        asset_prices = self.asset_prices.to_dict()

        gas_used = self.gas_used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "chainId": chain_id,
                "txHash": tx_hash,
                "blockNumber": block_number,
                "timestamp": timestamp,
                "action": action,
                "origin": origin,
                "market": market,
                "inputs": inputs,
                "outputs": outputs,
                "user": user,
                "valuation": valuation,
                "implicitSwapFeeSy": implicit_swap_fee_sy,
                "explicitSwapFeeSy": explicit_swap_fee_sy,
                "impliedApy": implied_apy,
                "assetPrices": asset_prices,
                "gasUsed": gas_used,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_amount_response import AssetAmountResponse
        from ..models.market_basic_response import MarketBasicResponse
        from ..models.transaction_response_asset_prices import TransactionResponseAssetPrices
        from ..models.valuation_response import ValuationResponse

        d = dict(src_dict)
        id = d.pop("id")

        chain_id = d.pop("chainId")

        tx_hash = d.pop("txHash")

        block_number = d.pop("blockNumber")

        timestamp = isoparse(d.pop("timestamp"))

        action = d.pop("action")

        origin = d.pop("origin")

        market = MarketBasicResponse.from_dict(d.pop("market"))

        inputs = []
        _inputs = d.pop("inputs")
        for inputs_item_data in _inputs:
            inputs_item = AssetAmountResponse.from_dict(inputs_item_data)

            inputs.append(inputs_item)

        outputs = []
        _outputs = d.pop("outputs")
        for outputs_item_data in _outputs:
            outputs_item = AssetAmountResponse.from_dict(outputs_item_data)

            outputs.append(outputs_item)

        user = d.pop("user")

        valuation = ValuationResponse.from_dict(d.pop("valuation"))

        implicit_swap_fee_sy = d.pop("implicitSwapFeeSy")

        explicit_swap_fee_sy = d.pop("explicitSwapFeeSy")

        implied_apy = d.pop("impliedApy")

        asset_prices = TransactionResponseAssetPrices.from_dict(d.pop("assetPrices"))

        gas_used = d.pop("gasUsed")

        transaction_response = cls(
            id=id,
            chain_id=chain_id,
            tx_hash=tx_hash,
            block_number=block_number,
            timestamp=timestamp,
            action=action,
            origin=origin,
            market=market,
            inputs=inputs,
            outputs=outputs,
            user=user,
            valuation=valuation,
            implicit_swap_fee_sy=implicit_swap_fee_sy,
            explicit_swap_fee_sy=explicit_swap_fee_sy,
            implied_apy=implied_apy,
            asset_prices=asset_prices,
            gas_used=gas_used,
        )

        transaction_response.additional_properties = d
        return transaction_response

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
