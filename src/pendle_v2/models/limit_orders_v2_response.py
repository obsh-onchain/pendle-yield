from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.limit_order_response import LimitOrderResponse


T = TypeVar("T", bound="LimitOrdersV2Response")


@_attrs_define
class LimitOrdersV2Response:
    """
    Attributes:
        total (float):
        limit (float):
        results (list['LimitOrderResponse']):
        resume_token (str):
    """

    total: float
    limit: float
    results: list["LimitOrderResponse"]
    resume_token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        limit = self.limit

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        resume_token = self.resume_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "limit": limit,
                "results": results,
                "resumeToken": resume_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.limit_order_response import LimitOrderResponse

        d = dict(src_dict)
        total = d.pop("total")

        limit = d.pop("limit")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = LimitOrderResponse.from_dict(results_item_data)

            results.append(results_item)

        resume_token = d.pop("resumeToken")

        limit_orders_v2_response = cls(
            total=total,
            limit=limit,
            results=results,
            resume_token=resume_token,
        )

        limit_orders_v2_response.additional_properties = d
        return limit_orders_v2_response

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
