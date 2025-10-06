from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.chain_id_simplified_data import ChainIdSimplifiedData


T = TypeVar("T", bound="GetSimplifiedDataResponse")


@_attrs_define
class GetSimplifiedDataResponse:
    """
    Attributes:
        data (list['ChainIdSimplifiedData']):
    """

    data: list["ChainIdSimplifiedData"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chain_id_simplified_data import ChainIdSimplifiedData

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ChainIdSimplifiedData.from_dict(data_item_data)

            data.append(data_item)

        get_simplified_data_response = cls(
            data=data,
        )

        get_simplified_data_response.additional_properties = d
        return get_simplified_data_response

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
