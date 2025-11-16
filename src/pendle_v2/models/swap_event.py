from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.swap_event_event_type import SwapEventEventType

if TYPE_CHECKING:
    from ..models.block_entity import BlockEntity
    from ..models.reserves import Reserves


T = TypeVar("T", bound="SwapEvent")


@_attrs_define
class SwapEvent:
    """
    Attributes:
        block (BlockEntity):
        txn_id (str): Transaction hash
        txn_index (float): Transaction index
        event_index (float): Event index
        maker (str): Transaction maker
        pair_id (str): Pair ID
        reserves (Reserves):
        event_type (SwapEventEventType): Type of event Example: swap.
        asset_0_in (str): Amount of token0 in
        asset_1_in (str): Amount of token1 in
        asset_0_out (str): Amount of token0 out
        asset_1_out (str): Amount of token1 out
        price_native (str): Price of asset0 quoted in asset1
    """

    block: "BlockEntity"
    txn_id: str
    txn_index: float
    event_index: float
    maker: str
    pair_id: str
    reserves: "Reserves"
    event_type: SwapEventEventType
    asset_0_in: str
    asset_1_in: str
    asset_0_out: str
    asset_1_out: str
    price_native: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block = self.block.to_dict()

        txn_id = self.txn_id

        txn_index = self.txn_index

        event_index = self.event_index

        maker = self.maker

        pair_id = self.pair_id

        reserves = self.reserves.to_dict()

        event_type = self.event_type.value

        asset_0_in = self.asset_0_in

        asset_1_in = self.asset_1_in

        asset_0_out = self.asset_0_out

        asset_1_out = self.asset_1_out

        price_native = self.price_native

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "block": block,
                "txnId": txn_id,
                "txnIndex": txn_index,
                "eventIndex": event_index,
                "maker": maker,
                "pairId": pair_id,
                "reserves": reserves,
                "eventType": event_type,
                "asset0In": asset_0_in,
                "asset1In": asset_1_in,
                "asset0Out": asset_0_out,
                "asset1Out": asset_1_out,
                "priceNative": price_native,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.block_entity import BlockEntity
        from ..models.reserves import Reserves

        d = dict(src_dict)
        block = BlockEntity.from_dict(d.pop("block"))

        txn_id = d.pop("txnId")

        txn_index = d.pop("txnIndex")

        event_index = d.pop("eventIndex")

        maker = d.pop("maker")

        pair_id = d.pop("pairId")

        reserves = Reserves.from_dict(d.pop("reserves"))

        event_type = SwapEventEventType(d.pop("eventType"))

        asset_0_in = d.pop("asset0In")

        asset_1_in = d.pop("asset1In")

        asset_0_out = d.pop("asset0Out")

        asset_1_out = d.pop("asset1Out")

        price_native = d.pop("priceNative")

        swap_event = cls(
            block=block,
            txn_id=txn_id,
            txn_index=txn_index,
            event_index=event_index,
            maker=maker,
            pair_id=pair_id,
            reserves=reserves,
            event_type=event_type,
            asset_0_in=asset_0_in,
            asset_1_in=asset_1_in,
            asset_0_out=asset_0_out,
            asset_1_out=asset_1_out,
            price_native=price_native,
        )

        swap_event.additional_properties = d
        return swap_event

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
