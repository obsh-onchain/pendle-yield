from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metadata_values_response_values_item_type_0 import MetadataValuesResponseValuesItemType0


T = TypeVar("T", bound="MetadataValuesResponse")


@_attrs_define
class MetadataValuesResponse:
    """
    Attributes:
        values (list[Union['MetadataValuesResponseValuesItemType0', None]]): Values of given metadata keys in the same
            order with keys
    """

    values: list[Union["MetadataValuesResponseValuesItemType0", None]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.metadata_values_response_values_item_type_0 import MetadataValuesResponseValuesItemType0

        values = []
        for values_item_data in self.values:
            values_item: Union[None, dict[str, Any]]
            if isinstance(values_item_data, MetadataValuesResponseValuesItemType0):
                values_item = values_item_data.to_dict()
            else:
                values_item = values_item_data
            values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_values_response_values_item_type_0 import MetadataValuesResponseValuesItemType0

        d = dict(src_dict)
        values = []
        _values = d.pop("values")
        for values_item_data in _values:

            def _parse_values_item(data: object) -> Union["MetadataValuesResponseValuesItemType0", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    values_item_type_0 = MetadataValuesResponseValuesItemType0.from_dict(data)

                    return values_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["MetadataValuesResponseValuesItemType0", None], data)

            values_item = _parse_values_item(values_item_data)

            values.append(values_item)

        metadata_values_response = cls(
            values=values,
        )

        metadata_values_response.additional_properties = d
        return metadata_values_response

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
