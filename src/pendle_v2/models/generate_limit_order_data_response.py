from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.generate_limit_order_data_response_order_type import GenerateLimitOrderDataResponseOrderType

T = TypeVar("T", bound="GenerateLimitOrderDataResponse")


@_attrs_define
class GenerateLimitOrderDataResponse:
    """
    Attributes:
        chain_id (float): Chain id
        yt (str): YT address
        salt (str): BigInt string of salt. Salt is a random generated number to distinguish between orders.Because of
            some technical reason, this number must be dividable by 12421
        expiry (str): Limit order expiry, in string
        nonce (str): Nonce of the limit order, this will help the maker to cancel all the limit order they created
        token (str): Input token if type is TOKEN_FOR_PT or TOKEN_FOR_YT, output token otherwise
        order_type (GenerateLimitOrderDataResponseOrderType): LimitOrderType { 0 : TOKEN_FOR_PT, 1 : PT_FOR_TOKEN, 2 :
            TOKEN_FOR_YT, 3 : YT_FOR_TOKEN }
        fail_safe_rate (str): BigInt string of failSafeRate
        maker (str): Maker's address
        receiver (str): Maker's address
        making_amount (str): BigInt string of making amount, the amount of token if the order is TOKEN_FOR_PT or
            TOKEN_FOR_YT, otherwise the amount of PT or YT
        permit (str):
        ln_implied_rate (int): ln(impliedRate) * 10**18, returned as bigint string
    """

    chain_id: float
    yt: str
    salt: str
    expiry: str
    nonce: str
    token: str
    order_type: GenerateLimitOrderDataResponseOrderType
    fail_safe_rate: str
    maker: str
    receiver: str
    making_amount: str
    permit: str
    ln_implied_rate: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chain_id = self.chain_id

        yt = self.yt

        salt = self.salt

        expiry = self.expiry

        nonce = self.nonce

        token = self.token

        order_type = self.order_type.value

        fail_safe_rate = self.fail_safe_rate

        maker = self.maker

        receiver = self.receiver

        making_amount = self.making_amount

        permit = self.permit

        ln_implied_rate = self.ln_implied_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chainId": chain_id,
                "YT": yt,
                "salt": salt,
                "expiry": expiry,
                "nonce": nonce,
                "token": token,
                "orderType": order_type,
                "failSafeRate": fail_safe_rate,
                "maker": maker,
                "receiver": receiver,
                "makingAmount": making_amount,
                "permit": permit,
                "lnImpliedRate": ln_implied_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chain_id = d.pop("chainId")

        yt = d.pop("YT")

        salt = d.pop("salt")

        expiry = d.pop("expiry")

        nonce = d.pop("nonce")

        token = d.pop("token")

        order_type = GenerateLimitOrderDataResponseOrderType(d.pop("orderType"))

        fail_safe_rate = d.pop("failSafeRate")

        maker = d.pop("maker")

        receiver = d.pop("receiver")

        making_amount = d.pop("makingAmount")

        permit = d.pop("permit")

        ln_implied_rate = d.pop("lnImpliedRate")

        generate_limit_order_data_response = cls(
            chain_id=chain_id,
            yt=yt,
            salt=salt,
            expiry=expiry,
            nonce=nonce,
            token=token,
            order_type=order_type,
            fail_safe_rate=fail_safe_rate,
            maker=maker,
            receiver=receiver,
            making_amount=making_amount,
            permit=permit,
            ln_implied_rate=ln_implied_rate,
        )

        generate_limit_order_data_response.additional_properties = d
        return generate_limit_order_data_response

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
