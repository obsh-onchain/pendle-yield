from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.generate_limit_order_data_dto_order_type import GenerateLimitOrderDataDtoOrderType

T = TypeVar("T", bound="GenerateLimitOrderDataDto")


@_attrs_define
class GenerateLimitOrderDataDto:
    """
    Attributes:
        chain_id (float): Chain Id
        yt (str): YT address
        order_type (GenerateLimitOrderDataDtoOrderType): LimitOrderType { 0 : TOKEN_FOR_PT, 1 : PT_FOR_TOKEN, 2 :
            TOKEN_FOR_YT, 3 : YT_FOR_TOKEN }
        token (str): Input token if type is TOKEN_FOR_PT or TOKEN_FOR_YT, output token otherwise
        maker (str): Maker address
        making_amount (str): BigInt string of making amount, the amount of token if the order is TOKEN_FOR_PT or
            TOKEN_FOR_YT, otherwise the amount of PT or YT
        implied_apy (float): Implied APY of this limit order
        expiry (str): Timestamp of order's expiry, in seconds
    """

    chain_id: float
    yt: str
    order_type: GenerateLimitOrderDataDtoOrderType
    token: str
    maker: str
    making_amount: str
    implied_apy: float
    expiry: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chain_id = self.chain_id

        yt = self.yt

        order_type = self.order_type.value

        token = self.token

        maker = self.maker

        making_amount = self.making_amount

        implied_apy = self.implied_apy

        expiry = self.expiry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chainId": chain_id,
                "YT": yt,
                "orderType": order_type,
                "token": token,
                "maker": maker,
                "makingAmount": making_amount,
                "impliedApy": implied_apy,
                "expiry": expiry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chain_id = d.pop("chainId")

        yt = d.pop("YT")

        order_type = GenerateLimitOrderDataDtoOrderType(d.pop("orderType"))

        token = d.pop("token")

        maker = d.pop("maker")

        making_amount = d.pop("makingAmount")

        implied_apy = d.pop("impliedApy")

        expiry = d.pop("expiry")

        generate_limit_order_data_dto = cls(
            chain_id=chain_id,
            yt=yt,
            order_type=order_type,
            token=token,
            maker=maker,
            making_amount=making_amount,
            implied_apy=implied_apy,
            expiry=expiry,
        )

        generate_limit_order_data_dto.additional_properties = d
        return generate_limit_order_data_dto

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
