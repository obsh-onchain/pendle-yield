import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TotalFeesWithTimestamp")


@_attrs_define
class TotalFeesWithTimestamp:
    """
    Attributes:
        time (datetime.datetime): timestamp where total fee is being calculated
        total_fees (Union[Unset, float]): total fees at given timestamp
    """

    time: datetime.datetime
    total_fees: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time.isoformat()

        total_fees = self.total_fees

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time": time,
            }
        )
        if total_fees is not UNSET:
            field_dict["totalFees"] = total_fees

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = isoparse(d.pop("time"))

        total_fees = d.pop("totalFees", UNSET)

        total_fees_with_timestamp = cls(
            time=time,
            total_fees=total_fees,
        )

        total_fees_with_timestamp.additional_properties = d
        return total_fees_with_timestamp

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
