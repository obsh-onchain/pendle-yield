from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_ve_pendle_cap_response_current_cap import GetVePendleCapResponseCurrentCap
    from ..models.get_ve_pendle_cap_response_expected_cap import GetVePendleCapResponseExpectedCap
    from ..models.get_ve_pendle_cap_response_fee import GetVePendleCapResponseFee


T = TypeVar("T", bound="GetVePendleCapResponse")


@_attrs_define
class GetVePendleCapResponse:
    """
    Attributes:
        fee (GetVePendleCapResponseFee):
        current_cap (GetVePendleCapResponseCurrentCap):
        expected_cap (GetVePendleCapResponseExpectedCap):
    """

    fee: "GetVePendleCapResponseFee"
    current_cap: "GetVePendleCapResponseCurrentCap"
    expected_cap: "GetVePendleCapResponseExpectedCap"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fee = self.fee.to_dict()

        current_cap = self.current_cap.to_dict()

        expected_cap = self.expected_cap.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fee": fee,
                "currentCap": current_cap,
                "expectedCap": expected_cap,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_ve_pendle_cap_response_current_cap import GetVePendleCapResponseCurrentCap
        from ..models.get_ve_pendle_cap_response_expected_cap import GetVePendleCapResponseExpectedCap
        from ..models.get_ve_pendle_cap_response_fee import GetVePendleCapResponseFee

        d = dict(src_dict)
        fee = GetVePendleCapResponseFee.from_dict(d.pop("fee"))

        current_cap = GetVePendleCapResponseCurrentCap.from_dict(d.pop("currentCap"))

        expected_cap = GetVePendleCapResponseExpectedCap.from_dict(d.pop("expectedCap"))

        get_ve_pendle_cap_response = cls(
            fee=fee,
            current_cap=current_cap,
            expected_cap=expected_cap,
        )

        get_ve_pendle_cap_response.additional_properties = d
        return get_ve_pendle_cap_response

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
