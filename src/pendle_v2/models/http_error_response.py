from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HttpErrorResponse")


@_attrs_define
class HttpErrorResponse:
    """
    Attributes:
        message (str):
        status_code (float):
        error (str):
    """

    message: str
    status_code: float
    error: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        status_code = self.status_code

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "statusCode": status_code,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        status_code = d.pop("statusCode")

        error = d.pop("error")

        http_error_response = cls(
            message=message,
            status_code=status_code,
            error=error,
        )

        http_error_response.additional_properties = d
        return http_error_response

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
