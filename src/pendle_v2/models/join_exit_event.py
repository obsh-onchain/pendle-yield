from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.join_exit_event_event_type import JoinExitEventEventType

if TYPE_CHECKING:
    from ..models.reserves import Reserves


T = TypeVar("T", bound="JoinExitEvent")


@_attrs_define
class JoinExitEvent:
    """
    Attributes:
        event_type (JoinExitEventEventType): Type of event
        txn_id (str): Transaction hash
        txn_index (float): Transaction index
        event_index (float): Event index
        maker (str): Transaction maker
        pair_id (str): Pair ID
        reserves (Reserves):
        amount0 (str): Amount of token0
        amount1 (str): Amount of token1
    """

    event_type: JoinExitEventEventType
    txn_id: str
    txn_index: float
    event_index: float
    maker: str
    pair_id: str
    reserves: "Reserves"
    amount0: str
    amount1: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        txn_id = self.txn_id

        txn_index = self.txn_index

        event_index = self.event_index

        maker = self.maker

        pair_id = self.pair_id

        reserves = self.reserves.to_dict()

        amount0 = self.amount0

        amount1 = self.amount1

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventType": event_type,
                "txnId": txn_id,
                "txnIndex": txn_index,
                "eventIndex": event_index,
                "maker": maker,
                "pairId": pair_id,
                "reserves": reserves,
                "amount0": amount0,
                "amount1": amount1,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reserves import Reserves

        d = dict(src_dict)
        event_type = JoinExitEventEventType(d.pop("eventType"))

        txn_id = d.pop("txnId")

        txn_index = d.pop("txnIndex")

        event_index = d.pop("eventIndex")

        maker = d.pop("maker")

        pair_id = d.pop("pairId")

        reserves = Reserves.from_dict(d.pop("reserves"))

        amount0 = d.pop("amount0")

        amount1 = d.pop("amount1")

        join_exit_event = cls(
            event_type=event_type,
            txn_id=txn_id,
            txn_index=txn_index,
            event_index=event_index,
            maker=maker,
            pair_id=pair_id,
            reserves=reserves,
            amount0=amount0,
            amount1=amount1,
        )

        join_exit_event.additional_properties = d
        return join_exit_event

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
