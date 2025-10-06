from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.market_meta_data import MarketMetaData
    from ..models.total_fees_with_timestamp import TotalFeesWithTimestamp


T = TypeVar("T", bound="MarketTotalFeesData")


@_attrs_define
class MarketTotalFeesData:
    """
    Attributes:
        market (MarketMetaData):
        values (list['TotalFeesWithTimestamp']): total fee at each timestamp
    """

    market: "MarketMetaData"
    values: list["TotalFeesWithTimestamp"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        market = self.market.to_dict()

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "market": market,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market_meta_data import MarketMetaData
        from ..models.total_fees_with_timestamp import TotalFeesWithTimestamp

        d = dict(src_dict)
        market = MarketMetaData.from_dict(d.pop("market"))

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = TotalFeesWithTimestamp.from_dict(values_item_data)

            values.append(values_item)

        market_total_fees_data = cls(
            market=market,
            values=values,
        )

        market_total_fees_data.additional_properties = d
        return market_total_fees_data

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
