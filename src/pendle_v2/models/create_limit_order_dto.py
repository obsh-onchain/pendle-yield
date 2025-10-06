from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_limit_order_dto_type import CreateLimitOrderDtoType

T = TypeVar("T", bound="CreateLimitOrderDto")


@_attrs_define
class CreateLimitOrderDto:
    """
    Attributes:
        chain_id (float): Chain Id
        signature (str): Signature of order, signed by maker
        salt (str): BigInt string of salt
        expiry (str): BigInt string of expiry
        nonce (str): BigInt string of nonce
        type_ (CreateLimitOrderDtoType): LimitOrderType { 0 : TOKEN_FOR_PT, 1 : PT_FOR_TOKEN, 2 : TOKEN_FOR_YT, 3 :
            YT_FOR_TOKEN }
        token (str): Token used by user to make order
        yt (str): YT address
        maker (str): Maker address
        receiver (str): Receiver address
        making_amount (str): BigInt string of making amount
        ln_implied_rate (str): BigInt string of lnImpliedRate
        fail_safe_rate (str): BigInt string of failSafeRate
        permit (str): Bytes string for permit
    """

    chain_id: float
    signature: str
    salt: str
    expiry: str
    nonce: str
    type_: CreateLimitOrderDtoType
    token: str
    yt: str
    maker: str
    receiver: str
    making_amount: str
    ln_implied_rate: str
    fail_safe_rate: str
    permit: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chain_id = self.chain_id

        signature = self.signature

        salt = self.salt

        expiry = self.expiry

        nonce = self.nonce

        type_ = self.type_.value

        token = self.token

        yt = self.yt

        maker = self.maker

        receiver = self.receiver

        making_amount = self.making_amount

        ln_implied_rate = self.ln_implied_rate

        fail_safe_rate = self.fail_safe_rate

        permit = self.permit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chainId": chain_id,
                "signature": signature,
                "salt": salt,
                "expiry": expiry,
                "nonce": nonce,
                "type": type_,
                "token": token,
                "yt": yt,
                "maker": maker,
                "receiver": receiver,
                "makingAmount": making_amount,
                "lnImpliedRate": ln_implied_rate,
                "failSafeRate": fail_safe_rate,
                "permit": permit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chain_id = d.pop("chainId")

        signature = d.pop("signature")

        salt = d.pop("salt")

        expiry = d.pop("expiry")

        nonce = d.pop("nonce")

        type_ = CreateLimitOrderDtoType(d.pop("type"))

        token = d.pop("token")

        yt = d.pop("yt")

        maker = d.pop("maker")

        receiver = d.pop("receiver")

        making_amount = d.pop("makingAmount")

        ln_implied_rate = d.pop("lnImpliedRate")

        fail_safe_rate = d.pop("failSafeRate")

        permit = d.pop("permit")

        create_limit_order_dto = cls(
            chain_id=chain_id,
            signature=signature,
            salt=salt,
            expiry=expiry,
            nonce=nonce,
            type_=type_,
            token=token,
            yt=yt,
            maker=maker,
            receiver=receiver,
            making_amount=making_amount,
            ln_implied_rate=ln_implied_rate,
            fail_safe_rate=fail_safe_rate,
            permit=permit,
        )

        create_limit_order_dto.additional_properties = d
        return create_limit_order_dto

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
