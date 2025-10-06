from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.utilized_protocol_response import UtilizedProtocolResponse


T = TypeVar("T", bound="GetAllUtilizedProtocolsResponse")


@_attrs_define
class GetAllUtilizedProtocolsResponse:
    """
    Attributes:
        results (list['UtilizedProtocolResponse']):
    """

    results: list["UtilizedProtocolResponse"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.utilized_protocol_response import UtilizedProtocolResponse

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = UtilizedProtocolResponse.from_dict(results_item_data)

            results.append(results_item)

        get_all_utilized_protocols_response = cls(
            results=results,
        )

        get_all_utilized_protocols_response.additional_properties = d
        return get_all_utilized_protocols_response

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
