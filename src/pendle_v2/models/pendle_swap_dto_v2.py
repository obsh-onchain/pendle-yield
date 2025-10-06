from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pendle_swap_input import PendleSwapInput


T = TypeVar("T", bound="PendleSwapDtoV2")


@_attrs_define
class PendleSwapDtoV2:
    """
    Attributes:
        receiver (str): The address to receive the output of the action
        inputs (list['PendleSwapInput']):
        token_out (str): Output token address
        slippage (float): Max slippage accepted. A value from 0 to 1 (0.01 is 1%)
        aggregators (Union[Unset, str]): List of aggregator names to use for the swap. If not provided, all aggregators
            will be used.List of supported aggregator can be found at:
            [getSupportedAggregators](#/SDK/SdkController_getSupportedAggregators) Example: kyberswap,okx.
    """

    receiver: str
    inputs: list["PendleSwapInput"]
    token_out: str
    slippage: float
    aggregators: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        receiver = self.receiver

        inputs = []
        for inputs_item_data in self.inputs:
            inputs_item = inputs_item_data.to_dict()
            inputs.append(inputs_item)

        token_out = self.token_out

        slippage = self.slippage

        aggregators = self.aggregators

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
        if aggregators is not UNSET:
            field_dict["aggregators"] = aggregators

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

        aggregators = d.pop("aggregators", UNSET)

        pendle_swap_dto_v2 = cls(
            receiver=receiver,
            inputs=inputs,
            token_out=token_out,
            slippage=slippage,
            aggregators=aggregators,
        )

        pendle_swap_dto_v2.additional_properties = d
        return pendle_swap_dto_v2

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
