from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.claim_token_amount import ClaimTokenAmount


T = TypeVar("T", bound="SyPosition")


@_attrs_define
class SyPosition:
    """
    Attributes:
        sy_id (str): Unique identifier of the market Example: 1-0xabc.
        balance (str): Sy token (SY) balance in wei Example: 1000000000000000000.
        claim_token_amounts (Union[Unset, list['ClaimTokenAmount']]): Array of claimable rewards
    """

    sy_id: str
    balance: str
    claim_token_amounts: Union[Unset, list["ClaimTokenAmount"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sy_id = self.sy_id

        balance = self.balance

        claim_token_amounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.claim_token_amounts, Unset):
            claim_token_amounts = []
            for claim_token_amounts_item_data in self.claim_token_amounts:
                claim_token_amounts_item = claim_token_amounts_item_data.to_dict()
                claim_token_amounts.append(claim_token_amounts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "syId": sy_id,
                "balance": balance,
            }
        )
        if claim_token_amounts is not UNSET:
            field_dict["claimTokenAmounts"] = claim_token_amounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claim_token_amount import ClaimTokenAmount

        d = dict(src_dict)
        sy_id = d.pop("syId")

        balance = d.pop("balance")

        claim_token_amounts = []
        _claim_token_amounts = d.pop("claimTokenAmounts", UNSET)
        for claim_token_amounts_item_data in _claim_token_amounts or []:
            claim_token_amounts_item = ClaimTokenAmount.from_dict(claim_token_amounts_item_data)

            claim_token_amounts.append(claim_token_amounts_item)

        sy_position = cls(
            sy_id=sy_id,
            balance=balance,
            claim_token_amounts=claim_token_amounts,
        )

        sy_position.additional_properties = d
        return sy_position

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
