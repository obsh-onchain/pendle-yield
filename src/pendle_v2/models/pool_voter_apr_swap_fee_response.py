from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pool_response import PoolResponse


T = TypeVar("T", bound="PoolVoterAprSwapFeeResponse")


@_attrs_define
class PoolVoterAprSwapFeeResponse:
    """
    Attributes:
        pool (PoolResponse):
        current_voter_apr (float):
        last_epoch_voter_apr (float):
        current_swap_fee (float):
        last_epoch_swap_fee (float):
        projected_voter_apr (float):
    """

    pool: "PoolResponse"
    current_voter_apr: float
    last_epoch_voter_apr: float
    current_swap_fee: float
    last_epoch_swap_fee: float
    projected_voter_apr: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pool = self.pool.to_dict()

        current_voter_apr = self.current_voter_apr

        last_epoch_voter_apr = self.last_epoch_voter_apr

        current_swap_fee = self.current_swap_fee

        last_epoch_swap_fee = self.last_epoch_swap_fee

        projected_voter_apr = self.projected_voter_apr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pool": pool,
                "currentVoterApr": current_voter_apr,
                "lastEpochVoterApr": last_epoch_voter_apr,
                "currentSwapFee": current_swap_fee,
                "lastEpochSwapFee": last_epoch_swap_fee,
                "projectedVoterApr": projected_voter_apr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pool_response import PoolResponse

        d = dict(src_dict)
        pool = PoolResponse.from_dict(d.pop("pool"))

        current_voter_apr = d.pop("currentVoterApr")

        last_epoch_voter_apr = d.pop("lastEpochVoterApr")

        current_swap_fee = d.pop("currentSwapFee")

        last_epoch_swap_fee = d.pop("lastEpochSwapFee")

        projected_voter_apr = d.pop("projectedVoterApr")

        pool_voter_apr_swap_fee_response = cls(
            pool=pool,
            current_voter_apr=current_voter_apr,
            last_epoch_voter_apr=last_epoch_voter_apr,
            current_swap_fee=current_swap_fee,
            last_epoch_swap_fee=last_epoch_swap_fee,
            projected_voter_apr=projected_voter_apr,
        )

        pool_voter_apr_swap_fee_response.additional_properties = d
        return pool_voter_apr_swap_fee_response

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
