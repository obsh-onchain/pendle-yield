from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metadata_response_results import MetadataResponseResults


T = TypeVar("T", bound="MetadataResponse")


@_attrs_define
class MetadataResponse:
    """
    Attributes:
        results (MetadataResponseResults):
        total (float):
    """

    results: "MetadataResponseResults"
    total: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = self.results.to_dict()

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_response_results import MetadataResponseResults

        d = dict(src_dict)
        results = MetadataResponseResults.from_dict(d.pop("results"))

        total = d.pop("total")

        metadata_response = cls(
            results=results,
            total=total,
        )

        metadata_response.additional_properties = d
        return metadata_response

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
