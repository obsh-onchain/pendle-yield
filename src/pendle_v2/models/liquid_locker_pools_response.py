from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.liquid_locker_pool_response import LiquidLockerPoolResponse


T = TypeVar("T", bound="LiquidLockerPoolsResponse")


@_attrs_define
class LiquidLockerPoolsResponse:
    """
    Attributes:
        total (float):
        results (list['LiquidLockerPoolResponse']):
    """

    total: float
    results: list["LiquidLockerPoolResponse"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.liquid_locker_pool_response import LiquidLockerPoolResponse

        d = dict(src_dict)
        total = d.pop("total")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = LiquidLockerPoolResponse.from_dict(results_item_data)

            results.append(results_item)

        liquid_locker_pools_response = cls(
            total=total,
            results=results,
        )

        liquid_locker_pools_response.additional_properties = d
        return liquid_locker_pools_response

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
