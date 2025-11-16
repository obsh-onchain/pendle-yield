from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetMonthlyRevenueResponse")


@_attrs_define
class GetMonthlyRevenueResponse:
    """
    Attributes:
        revenues (list[float]): The revenues of the month in USD within the time range
        epoch_start_dates (list[str]): The start dates of the month in Date within the time range
        accumulated_revenue (float): all time revenues in USD
    """

    revenues: list[float]
    epoch_start_dates: list[str]
    accumulated_revenue: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revenues = self.revenues

        epoch_start_dates = self.epoch_start_dates

        accumulated_revenue = self.accumulated_revenue

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revenues": revenues,
                "epochStartDates": epoch_start_dates,
                "accumulatedRevenue": accumulated_revenue,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        revenues = cast(list[float], d.pop("revenues"))

        epoch_start_dates = cast(list[str], d.pop("epochStartDates"))

        accumulated_revenue = d.pop("accumulatedRevenue")

        get_monthly_revenue_response = cls(
            revenues=revenues,
            epoch_start_dates=epoch_start_dates,
            accumulated_revenue=accumulated_revenue,
        )

        get_monthly_revenue_response.additional_properties = d
        return get_monthly_revenue_response

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
