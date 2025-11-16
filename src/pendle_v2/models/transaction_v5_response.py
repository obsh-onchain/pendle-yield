import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notional_v5 import NotionalV5


T = TypeVar("T", bound="TransactionV5Response")


@_attrs_define
class TransactionV5Response:
    """
    Attributes:
        id (str): Unique identifier of the transaction
        market (str): Market address where the transaction occurred
        timestamp (datetime.datetime): Timestamp when the transaction occurred
        chain_id (float): Chain ID where the transaction occurred
        tx_hash (str): Transaction hash on the blockchain
        value (float): Transaction value in USD
        type_ (str): Transaction type (e.g., TRADES, ADD_LIQUIDITY, REMOVE_LIQUIDITY)
        action (str): Transaction action (e.g., BUY_PT, SELL_PT, ADD_LIQUIDITY_DUAL)
        implied_apy (float): Weighted average implied APY for this transaction
        tx_origin (Union[Unset, str]): Original transaction sender address
        notional (Union[Unset, NotionalV5]):
    """

    id: str
    market: str
    timestamp: datetime.datetime
    chain_id: float
    tx_hash: str
    value: float
    type_: str
    action: str
    implied_apy: float
    tx_origin: Union[Unset, str] = UNSET
    notional: Union[Unset, "NotionalV5"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        market = self.market

        timestamp = self.timestamp.isoformat()

        chain_id = self.chain_id

        tx_hash = self.tx_hash

        value = self.value

        type_ = self.type_

        action = self.action

        implied_apy = self.implied_apy

        tx_origin = self.tx_origin

        notional: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.notional, Unset):
            notional = self.notional.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "market": market,
                "timestamp": timestamp,
                "chainId": chain_id,
                "txHash": tx_hash,
                "value": value,
                "type": type_,
                "action": action,
                "impliedApy": implied_apy,
            }
        )
        if tx_origin is not UNSET:
            field_dict["txOrigin"] = tx_origin
        if notional is not UNSET:
            field_dict["notional"] = notional

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notional_v5 import NotionalV5

        d = dict(src_dict)
        id = d.pop("id")

        market = d.pop("market")

        timestamp = isoparse(d.pop("timestamp"))

        chain_id = d.pop("chainId")

        tx_hash = d.pop("txHash")

        value = d.pop("value")

        type_ = d.pop("type")

        action = d.pop("action")

        implied_apy = d.pop("impliedApy")

        tx_origin = d.pop("txOrigin", UNSET)

        _notional = d.pop("notional", UNSET)
        notional: Union[Unset, NotionalV5]
        if isinstance(_notional, Unset):
            notional = UNSET
        else:
            notional = NotionalV5.from_dict(_notional)

        transaction_v5_response = cls(
            id=id,
            market=market,
            timestamp=timestamp,
            chain_id=chain_id,
            tx_hash=tx_hash,
            value=value,
            type_=type_,
            action=action,
            implied_apy=implied_apy,
            tx_origin=tx_origin,
            notional=notional,
        )

        transaction_v5_response.additional_properties = d
        return transaction_v5_response

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
