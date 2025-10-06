from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionsV4Response")


@_attrs_define
class TransactionsV4Response:
    """
    Attributes:
        total (float):
        limit (float):
        skip (float):
        results (list[str]):
        resume_token (Union[Unset, str]): Resume token for pagination. Use this to continue a previous query. Use this
            token in the next request. Can be undefined if the query is at the end of the results.
    """

    total: float
    limit: float
    skip: float
    results: list[str]
    resume_token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        limit = self.limit

        skip = self.skip

        results = self.results

        resume_token = self.resume_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "limit": limit,
                "skip": skip,
                "results": results,
            }
        )
        if resume_token is not UNSET:
            field_dict["resumeToken"] = resume_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        limit = d.pop("limit")

        skip = d.pop("skip")

        results = cast(list[str], d.pop("results"))

        resume_token = d.pop("resumeToken", UNSET)

        transactions_v4_response = cls(
            total=total,
            limit=limit,
            skip=skip,
            results=results,
            resume_token=resume_token,
        )

        transactions_v4_response.additional_properties = d
        return transactions_v4_response

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
