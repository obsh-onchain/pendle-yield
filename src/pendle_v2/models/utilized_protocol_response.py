from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UtilizedProtocolResponse")


@_attrs_define
class UtilizedProtocolResponse:
    """
    Attributes:
        id (str):
        url (str):
        name (str):
        image_url (str):
    """

    id: str
    url: str
    name: str
    image_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        name = self.name

        image_url = self.image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "name": name,
                "imageUrl": image_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        name = d.pop("name")

        image_url = d.pop("imageUrl")

        utilized_protocol_response = cls(
            id=id,
            url=url,
            name=name,
            image_url=image_url,
        )

        utilized_protocol_response.additional_properties = d
        return utilized_protocol_response

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
