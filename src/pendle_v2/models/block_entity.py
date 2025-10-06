from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BlockEntity")


@_attrs_define
class BlockEntity:
    """
    Attributes:
        block_number (float): Block number
        block_timestamp (float): Block timestamp in seconds
    """

    block_number: float
    block_timestamp: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block_number = self.block_number

        block_timestamp = self.block_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blockNumber": block_number,
                "blockTimestamp": block_timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        block_number = d.pop("blockNumber")

        block_timestamp = d.pop("blockTimestamp")

        block_entity = cls(
            block_number=block_number,
            block_timestamp=block_timestamp,
        )

        block_entity.additional_properties = d
        return block_entity

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
