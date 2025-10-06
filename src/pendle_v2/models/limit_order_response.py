import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.limit_order_response_status import LimitOrderResponseStatus
from ..models.limit_order_response_type import LimitOrderResponseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_filled_status_response import OrderFilledStatusResponse
    from ..models.order_state_response import OrderStateResponse


T = TypeVar("T", bound="LimitOrderResponse")


@_attrs_define
class LimitOrderResponse:
    """
    Attributes:
        id (str): Hash of the order
        signature (str): Signature of order, signed by maker
        chain_id (float): Chain id
        salt (str): BigInt string of salt
        expiry (str): BigInt string of expiry, in second
        nonce (str): BigInt string of nonce
        type_ (LimitOrderResponseType): LimitOrderType { 0 : TOKEN_FOR_PT, 1 : PT_FOR_TOKEN, 2 : TOKEN_FOR_YT, 3 :
            YT_FOR_TOKEN }
        token (str): Token used by user to make order
        yt (str): YT address
        maker (str): Maker address
        receiver (str): Receiver address
        making_amount (str): BigInt string of making amount, the amount of token if the order is TOKEN_FOR_PT or
            TOKEN_FOR_YT, otherwise the amount of PT or YT
        current_making_amount (str): BigInt string of remaining making amount, the unit is the same as makingAmount
        ln_implied_rate (str): BigInt string of lnImpliedRate
        fail_safe_rate (str): BigInt string of failSafeRate
        permit (str): Bytes string for permit
        order_filled_status (OrderFilledStatusResponse):
        is_active (bool):
        is_canceled (bool):
        created_at (datetime.datetime):
        sy (str): SY address
        pt (str): PT address
        maker_balance (str): Min(maker balance, maker allowance)
        failed_mint_sy (bool): Simulate result of the order to mint sy
        failed_mint_sy_reason (str): Error reason of the order to mint sy
        order_book_balance (str): Bigint string of amount shown on order book
        making_token (str): Making token address
        taking_token (str): Taking token address
        status (LimitOrderResponseStatus): LimitOrderStatus
        order_state (Union[Unset, OrderStateResponse]):
        fully_executed_timestamp (Union[Unset, datetime.datetime]): Fully filled timestamp
        canceled_timestamp (Union[Unset, datetime.datetime]): Canceled timestamp
        latest_event_timestamp (Union[Unset, datetime.datetime]): Timestamp of latest event
    """

    id: str
    signature: str
    chain_id: float
    salt: str
    expiry: str
    nonce: str
    type_: LimitOrderResponseType
    token: str
    yt: str
    maker: str
    receiver: str
    making_amount: str
    current_making_amount: str
    ln_implied_rate: str
    fail_safe_rate: str
    permit: str
    order_filled_status: "OrderFilledStatusResponse"
    is_active: bool
    is_canceled: bool
    created_at: datetime.datetime
    sy: str
    pt: str
    maker_balance: str
    failed_mint_sy: bool
    failed_mint_sy_reason: str
    order_book_balance: str
    making_token: str
    taking_token: str
    status: LimitOrderResponseStatus
    order_state: Union[Unset, "OrderStateResponse"] = UNSET
    fully_executed_timestamp: Union[Unset, datetime.datetime] = UNSET
    canceled_timestamp: Union[Unset, datetime.datetime] = UNSET
    latest_event_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        signature = self.signature

        chain_id = self.chain_id

        salt = self.salt

        expiry = self.expiry

        nonce = self.nonce

        type_ = self.type_.value

        token = self.token

        yt = self.yt

        maker = self.maker

        receiver = self.receiver

        making_amount = self.making_amount

        current_making_amount = self.current_making_amount

        ln_implied_rate = self.ln_implied_rate

        fail_safe_rate = self.fail_safe_rate

        permit = self.permit

        order_filled_status = self.order_filled_status.to_dict()

        is_active = self.is_active

        is_canceled = self.is_canceled

        created_at = self.created_at.isoformat()

        sy = self.sy

        pt = self.pt

        maker_balance = self.maker_balance

        failed_mint_sy = self.failed_mint_sy

        failed_mint_sy_reason = self.failed_mint_sy_reason

        order_book_balance = self.order_book_balance

        making_token = self.making_token

        taking_token = self.taking_token

        status = self.status.value

        order_state: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order_state, Unset):
            order_state = self.order_state.to_dict()

        fully_executed_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.fully_executed_timestamp, Unset):
            fully_executed_timestamp = self.fully_executed_timestamp.isoformat()

        canceled_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.canceled_timestamp, Unset):
            canceled_timestamp = self.canceled_timestamp.isoformat()

        latest_event_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.latest_event_timestamp, Unset):
            latest_event_timestamp = self.latest_event_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "signature": signature,
                "chainId": chain_id,
                "salt": salt,
                "expiry": expiry,
                "nonce": nonce,
                "type": type_,
                "token": token,
                "yt": yt,
                "maker": maker,
                "receiver": receiver,
                "makingAmount": making_amount,
                "currentMakingAmount": current_making_amount,
                "lnImpliedRate": ln_implied_rate,
                "failSafeRate": fail_safe_rate,
                "permit": permit,
                "orderFilledStatus": order_filled_status,
                "isActive": is_active,
                "isCanceled": is_canceled,
                "createdAt": created_at,
                "sy": sy,
                "pt": pt,
                "makerBalance": maker_balance,
                "failedMintSy": failed_mint_sy,
                "failedMintSyReason": failed_mint_sy_reason,
                "orderBookBalance": order_book_balance,
                "makingToken": making_token,
                "takingToken": taking_token,
                "status": status,
            }
        )
        if order_state is not UNSET:
            field_dict["orderState"] = order_state
        if fully_executed_timestamp is not UNSET:
            field_dict["fullyExecutedTimestamp"] = fully_executed_timestamp
        if canceled_timestamp is not UNSET:
            field_dict["canceledTimestamp"] = canceled_timestamp
        if latest_event_timestamp is not UNSET:
            field_dict["latestEventTimestamp"] = latest_event_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_filled_status_response import OrderFilledStatusResponse
        from ..models.order_state_response import OrderStateResponse

        d = dict(src_dict)
        id = d.pop("id")

        signature = d.pop("signature")

        chain_id = d.pop("chainId")

        salt = d.pop("salt")

        expiry = d.pop("expiry")

        nonce = d.pop("nonce")

        type_ = LimitOrderResponseType(d.pop("type"))

        token = d.pop("token")

        yt = d.pop("yt")

        maker = d.pop("maker")

        receiver = d.pop("receiver")

        making_amount = d.pop("makingAmount")

        current_making_amount = d.pop("currentMakingAmount")

        ln_implied_rate = d.pop("lnImpliedRate")

        fail_safe_rate = d.pop("failSafeRate")

        permit = d.pop("permit")

        order_filled_status = OrderFilledStatusResponse.from_dict(d.pop("orderFilledStatus"))

        is_active = d.pop("isActive")

        is_canceled = d.pop("isCanceled")

        created_at = isoparse(d.pop("createdAt"))

        sy = d.pop("sy")

        pt = d.pop("pt")

        maker_balance = d.pop("makerBalance")

        failed_mint_sy = d.pop("failedMintSy")

        failed_mint_sy_reason = d.pop("failedMintSyReason")

        order_book_balance = d.pop("orderBookBalance")

        making_token = d.pop("makingToken")

        taking_token = d.pop("takingToken")

        status = LimitOrderResponseStatus(d.pop("status"))

        _order_state = d.pop("orderState", UNSET)
        order_state: Union[Unset, OrderStateResponse]
        if isinstance(_order_state, Unset):
            order_state = UNSET
        else:
            order_state = OrderStateResponse.from_dict(_order_state)

        _fully_executed_timestamp = d.pop("fullyExecutedTimestamp", UNSET)
        fully_executed_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_fully_executed_timestamp, Unset):
            fully_executed_timestamp = UNSET
        else:
            fully_executed_timestamp = isoparse(_fully_executed_timestamp)

        _canceled_timestamp = d.pop("canceledTimestamp", UNSET)
        canceled_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_canceled_timestamp, Unset):
            canceled_timestamp = UNSET
        else:
            canceled_timestamp = isoparse(_canceled_timestamp)

        _latest_event_timestamp = d.pop("latestEventTimestamp", UNSET)
        latest_event_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_latest_event_timestamp, Unset):
            latest_event_timestamp = UNSET
        else:
            latest_event_timestamp = isoparse(_latest_event_timestamp)

        limit_order_response = cls(
            id=id,
            signature=signature,
            chain_id=chain_id,
            salt=salt,
            expiry=expiry,
            nonce=nonce,
            type_=type_,
            token=token,
            yt=yt,
            maker=maker,
            receiver=receiver,
            making_amount=making_amount,
            current_making_amount=current_making_amount,
            ln_implied_rate=ln_implied_rate,
            fail_safe_rate=fail_safe_rate,
            permit=permit,
            order_filled_status=order_filled_status,
            is_active=is_active,
            is_canceled=is_canceled,
            created_at=created_at,
            sy=sy,
            pt=pt,
            maker_balance=maker_balance,
            failed_mint_sy=failed_mint_sy,
            failed_mint_sy_reason=failed_mint_sy_reason,
            order_book_balance=order_book_balance,
            making_token=making_token,
            taking_token=taking_token,
            status=status,
            order_state=order_state,
            fully_executed_timestamp=fully_executed_timestamp,
            canceled_timestamp=canceled_timestamp,
            latest_event_timestamp=latest_event_timestamp,
        )

        limit_order_response.additional_properties = d
        return limit_order_response

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
