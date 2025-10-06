from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pendle_swap_input import PendleSwapInput


T = TypeVar("T", bound="PendleSwapDto")


@_attrs_define
class PendleSwapDto:
    """
    Attributes:
        receiver (str): The address to receive the output of the action
        inputs (list['PendleSwapInput']):
        token_out (str): Output token address
        slippage (float): Max slippage accepted. A value from 0 to 1 (0.01 is 1%)
    """

    receiver: str
    inputs: list["PendleSwapInput"]
    token_out: str
    slippage: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        receiver = self.receiver

        inputs = []
        for inputs_item_data in self.inputs:
            inputs_item = inputs_item_data.to_dict()
            inputs.append(inputs_item)

        token_out = self.token_out

        slippage = self.slippage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "receiver": receiver,
                "inputs": inputs,
                "tokenOut": token_out,
                "slippage": slippage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pendle_swap_input import PendleSwapInput

        d = dict(src_dict)
        receiver = d.pop("receiver")

        inputs = []
        _inputs = d.pop("inputs")
        for inputs_item_data in _inputs:
            inputs_item = PendleSwapInput.from_dict(inputs_item_data)

            inputs.append(inputs_item)

        token_out = d.pop("tokenOut")

        slippage = d.pop("slippage")

        pendle_swap_dto = cls(
            receiver=receiver,
            inputs=inputs,
            token_out=token_out,
            slippage=slippage,
        )

        pendle_swap_dto.additional_properties = d
        return pendle_swap_dto

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
