import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.pool_voter_apr_swap_fee_response import PoolVoterAprSwapFeeResponse


T = TypeVar("T", bound="PoolVoterAprsSwapFeesResponse")


@_attrs_define
class PoolVoterAprsSwapFeesResponse:
    """
    Attributes:
        results (list['PoolVoterAprSwapFeeResponse']):
        total_pools (float):
        total_fee (float):
        timestamp (datetime.datetime):
    """

    results: list["PoolVoterAprSwapFeeResponse"]
    total_pools: float
    total_fee: float
    timestamp: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        total_pools = self.total_pools

        total_fee = self.total_fee

        timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "totalPools": total_pools,
                "totalFee": total_fee,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pool_voter_apr_swap_fee_response import PoolVoterAprSwapFeeResponse

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = PoolVoterAprSwapFeeResponse.from_dict(results_item_data)

            results.append(results_item)

        total_pools = d.pop("totalPools")

        total_fee = d.pop("totalFee")

        timestamp = isoparse(d.pop("timestamp"))

        pool_voter_aprs_swap_fees_response = cls(
            results=results,
            total_pools=total_pools,
            total_fee=total_fee,
            timestamp=timestamp,
        )

        pool_voter_aprs_swap_fees_response.additional_properties = d
        return pool_voter_aprs_swap_fees_response

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
