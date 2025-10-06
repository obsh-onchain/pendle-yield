from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.market_data import MarketData


T = TypeVar("T", bound="GetInactiveMarketsResponse")


@_attrs_define
class GetInactiveMarketsResponse:
    """
    Attributes:
        markets (list['MarketData']): inactive market list Example: [{'name': 'crvUSD', 'address':
            '0x386f90eb964a477498b528a39d9405e73ed4032b', 'expiry': '2024-03-28T00:00:00.000Z', 'pt':
            '1-0xb87511364014c088e30f872efc4a00d7efb843ac', 'yt': '1-0xed97f94dd94255637a054098604e0201c442a3fd', 'sy':
            '1-0xe05082b184a34668cd8a904d85fa815802bbb04c', 'underlyingAsset':
            '1-0xb27d1729489d04473631f0afaca3c3a7389ac9f8', 'details': {'liquidity': 1000000, 'pendleApy': 0.05,
            'impliedApy': 0.05, 'feeRate': 0.001, 'yieldRange': {'min': 0.01, 'max': 0.02}, 'aggregatedApy': 0.1,
            'maxBoostedApy': 0.1}, 'isNew': True, 'isPrime': True, 'timestamp': '2025-03-18T00:00:00.000Z', 'categoryIds':
            ['stables']}, {'name': 'USD0++', 'address': '0x64506968e80c9ed07bff60c8d9d57474effff2c9', 'expiry':
            '2025-01-30T00:00:00.000Z', 'pt': '1-0x61439b9575278054d69c9176d88fafaf8319e4b7', 'yt':
            '1-0x9697e1ef258b847275e1b32f8a57b3a7e2f8ec50', 'sy': '1-0x52453825c287ddef62d647ce51c0979d27c461f7',
            'underlyingAsset': '1-0x35d8949372d46b7a3d5a56006ae77b215fc69bc0', 'details': {'liquidity': 1000000,
            'pendleApy': 0.05, 'impliedApy': 0.05, 'feeRate': 0.001, 'yieldRange': {'min': 0.01, 'max': 0.02},
            'aggregatedApy': 0.1, 'maxBoostedApy': 0.1}, 'isNew': False, 'isPrime': False, 'timestamp':
            '2025-02-18T00:00:00.000Z', 'categoryIds': ['rwa']}].
    """

    markets: list["MarketData"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        markets = []
        for markets_item_data in self.markets:
            markets_item = markets_item_data.to_dict()
            markets.append(markets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "markets": markets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market_data import MarketData

        d = dict(src_dict)
        markets = []
        _markets = d.pop("markets")
        for markets_item_data in _markets:
            markets_item = MarketData.from_dict(markets_item_data)

            markets.append(markets_item)

        get_inactive_markets_response = cls(
            markets=markets,
        )

        get_inactive_markets_response.additional_properties = d
        return get_inactive_markets_response

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
