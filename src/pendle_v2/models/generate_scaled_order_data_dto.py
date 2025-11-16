from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.generate_scaled_order_data_dto_order_type import GenerateScaledOrderDataDtoOrderType
from ..models.generate_scaled_order_data_dto_size_distribution import GenerateScaledOrderDataDtoSizeDistribution

T = TypeVar("T", bound="GenerateScaledOrderDataDto")


@_attrs_define
class GenerateScaledOrderDataDto:
    """
    Attributes:
        chain_id (float): Chain Id
        yt (str): YT address
        order_type (GenerateScaledOrderDataDtoOrderType): LimitOrderType { 0 : TOKEN_FOR_PT, 1 : PT_FOR_TOKEN, 2 :
            TOKEN_FOR_YT, 3 : YT_FOR_TOKEN }
        token (str): Input token if type is TOKEN_FOR_PT or TOKEN_FOR_YT, output token otherwise
        maker (str): Maker address
        making_amount (str): BigInt string of making amount, the amount of token if the order is TOKEN_FOR_PT or
            TOKEN_FOR_YT, otherwise the amount of PT or YT
        lower_implied_apy (float): Lower implied APY of this scaled order
        upper_implied_apy (float): Upper implied APY of this scaled order
        order_count (float): Upper implied APY of this scaled order
        size_distribution (GenerateScaledOrderDataDtoSizeDistribution): Scaled Order Distribution Type {  }
        expiry (str): Timestamp of order's expiry, in seconds
    """

    chain_id: float
    yt: str
    order_type: GenerateScaledOrderDataDtoOrderType
    token: str
    maker: str
    making_amount: str
    lower_implied_apy: float
    upper_implied_apy: float
    order_count: float
    size_distribution: GenerateScaledOrderDataDtoSizeDistribution
    expiry: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chain_id = self.chain_id

        yt = self.yt

        order_type = self.order_type.value

        token = self.token

        maker = self.maker

        making_amount = self.making_amount

        lower_implied_apy = self.lower_implied_apy

        upper_implied_apy = self.upper_implied_apy

        order_count = self.order_count

        size_distribution = self.size_distribution.value

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
                "lowerImpliedApy": lower_implied_apy,
                "upperImpliedApy": upper_implied_apy,
                "orderCount": order_count,
                "sizeDistribution": size_distribution,
                "expiry": expiry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chain_id = d.pop("chainId")

        yt = d.pop("YT")

        order_type = GenerateScaledOrderDataDtoOrderType(d.pop("orderType"))

        token = d.pop("token")

        maker = d.pop("maker")

        making_amount = d.pop("makingAmount")

        lower_implied_apy = d.pop("lowerImpliedApy")

        upper_implied_apy = d.pop("upperImpliedApy")

        order_count = d.pop("orderCount")

        size_distribution = GenerateScaledOrderDataDtoSizeDistribution(d.pop("sizeDistribution"))

        expiry = d.pop("expiry")

        generate_scaled_order_data_dto = cls(
            chain_id=chain_id,
            yt=yt,
            order_type=order_type,
            token=token,
            maker=maker,
            making_amount=making_amount,
            lower_implied_apy=lower_implied_apy,
            upper_implied_apy=upper_implied_apy,
            order_count=order_count,
            size_distribution=size_distribution,
            expiry=expiry,
        )

        generate_scaled_order_data_dto.additional_properties = d
        return generate_scaled_order_data_dto

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
