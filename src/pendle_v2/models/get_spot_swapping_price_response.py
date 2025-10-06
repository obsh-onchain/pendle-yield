from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_spot_swapping_price_response_pt_to_underlying_token_rate_type_0 import (
        GetSpotSwappingPriceResponsePtToUnderlyingTokenRateType0,
    )
    from ..models.get_spot_swapping_price_response_underlying_token_to_pt_rate_type_0 import (
        GetSpotSwappingPriceResponseUnderlyingTokenToPtRateType0,
    )
    from ..models.get_spot_swapping_price_response_underlying_token_to_yt_rate_type_0 import (
        GetSpotSwappingPriceResponseUnderlyingTokenToYtRateType0,
    )
    from ..models.get_spot_swapping_price_response_yt_to_underlying_token_rate_type_0 import (
        GetSpotSwappingPriceResponseYtToUnderlyingTokenRateType0,
    )


T = TypeVar("T", bound="GetSpotSwappingPriceResponse")


@_attrs_define
class GetSpotSwappingPriceResponse:
    """
    Attributes:
        underlying_token (str): underlying token address that will be used for swapping
        underlying_token_to_pt_rate (Union['GetSpotSwappingPriceResponseUnderlyingTokenToPtRateType0', None]): number of
            PT by swapping 1 underlying token. If the swap can not be done, this value will be null
        pt_to_underlying_token_rate (Union['GetSpotSwappingPriceResponsePtToUnderlyingTokenRateType0', None]): number of
            underlying token by swapping 1 PT. If the swap can not be done, this value will be null
        underlying_token_to_yt_rate (Union['GetSpotSwappingPriceResponseUnderlyingTokenToYtRateType0', None]): number of
            YT by swapping 1 underlying token. If the swap can not be done, this value will be null
        yt_to_underlying_token_rate (Union['GetSpotSwappingPriceResponseYtToUnderlyingTokenRateType0', None]): number of
            underlying token by swapping 1 YT. If the swap can not be done, this value will be null
        implied_apy (float): implied apy of the given market
    """

    underlying_token: str
    underlying_token_to_pt_rate: Union["GetSpotSwappingPriceResponseUnderlyingTokenToPtRateType0", None]
    pt_to_underlying_token_rate: Union["GetSpotSwappingPriceResponsePtToUnderlyingTokenRateType0", None]
    underlying_token_to_yt_rate: Union["GetSpotSwappingPriceResponseUnderlyingTokenToYtRateType0", None]
    yt_to_underlying_token_rate: Union["GetSpotSwappingPriceResponseYtToUnderlyingTokenRateType0", None]
    implied_apy: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_spot_swapping_price_response_pt_to_underlying_token_rate_type_0 import (
            GetSpotSwappingPriceResponsePtToUnderlyingTokenRateType0,
        )
        from ..models.get_spot_swapping_price_response_underlying_token_to_pt_rate_type_0 import (
            GetSpotSwappingPriceResponseUnderlyingTokenToPtRateType0,
        )
        from ..models.get_spot_swapping_price_response_underlying_token_to_yt_rate_type_0 import (
            GetSpotSwappingPriceResponseUnderlyingTokenToYtRateType0,
        )
        from ..models.get_spot_swapping_price_response_yt_to_underlying_token_rate_type_0 import (
            GetSpotSwappingPriceResponseYtToUnderlyingTokenRateType0,
        )

        underlying_token = self.underlying_token

        underlying_token_to_pt_rate: Union[None, dict[str, Any]]
        if isinstance(self.underlying_token_to_pt_rate, GetSpotSwappingPriceResponseUnderlyingTokenToPtRateType0):
            underlying_token_to_pt_rate = self.underlying_token_to_pt_rate.to_dict()
        else:
            underlying_token_to_pt_rate = self.underlying_token_to_pt_rate

        pt_to_underlying_token_rate: Union[None, dict[str, Any]]
        if isinstance(self.pt_to_underlying_token_rate, GetSpotSwappingPriceResponsePtToUnderlyingTokenRateType0):
            pt_to_underlying_token_rate = self.pt_to_underlying_token_rate.to_dict()
        else:
            pt_to_underlying_token_rate = self.pt_to_underlying_token_rate

        underlying_token_to_yt_rate: Union[None, dict[str, Any]]
        if isinstance(self.underlying_token_to_yt_rate, GetSpotSwappingPriceResponseUnderlyingTokenToYtRateType0):
            underlying_token_to_yt_rate = self.underlying_token_to_yt_rate.to_dict()
        else:
            underlying_token_to_yt_rate = self.underlying_token_to_yt_rate

        yt_to_underlying_token_rate: Union[None, dict[str, Any]]
        if isinstance(self.yt_to_underlying_token_rate, GetSpotSwappingPriceResponseYtToUnderlyingTokenRateType0):
            yt_to_underlying_token_rate = self.yt_to_underlying_token_rate.to_dict()
        else:
            yt_to_underlying_token_rate = self.yt_to_underlying_token_rate

        implied_apy = self.implied_apy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "underlyingToken": underlying_token,
                "underlyingTokenToPtRate": underlying_token_to_pt_rate,
                "ptToUnderlyingTokenRate": pt_to_underlying_token_rate,
                "underlyingTokenToYtRate": underlying_token_to_yt_rate,
                "ytToUnderlyingTokenRate": yt_to_underlying_token_rate,
                "impliedApy": implied_apy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_spot_swapping_price_response_pt_to_underlying_token_rate_type_0 import (
            GetSpotSwappingPriceResponsePtToUnderlyingTokenRateType0,
        )
        from ..models.get_spot_swapping_price_response_underlying_token_to_pt_rate_type_0 import (
            GetSpotSwappingPriceResponseUnderlyingTokenToPtRateType0,
        )
        from ..models.get_spot_swapping_price_response_underlying_token_to_yt_rate_type_0 import (
            GetSpotSwappingPriceResponseUnderlyingTokenToYtRateType0,
        )
        from ..models.get_spot_swapping_price_response_yt_to_underlying_token_rate_type_0 import (
            GetSpotSwappingPriceResponseYtToUnderlyingTokenRateType0,
        )

        d = dict(src_dict)
        underlying_token = d.pop("underlyingToken")

        def _parse_underlying_token_to_pt_rate(
            data: object,
        ) -> Union["GetSpotSwappingPriceResponseUnderlyingTokenToPtRateType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                underlying_token_to_pt_rate_type_0 = GetSpotSwappingPriceResponseUnderlyingTokenToPtRateType0.from_dict(
                    data
                )

                return underlying_token_to_pt_rate_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GetSpotSwappingPriceResponseUnderlyingTokenToPtRateType0", None], data)

        underlying_token_to_pt_rate = _parse_underlying_token_to_pt_rate(d.pop("underlyingTokenToPtRate"))

        def _parse_pt_to_underlying_token_rate(
            data: object,
        ) -> Union["GetSpotSwappingPriceResponsePtToUnderlyingTokenRateType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pt_to_underlying_token_rate_type_0 = GetSpotSwappingPriceResponsePtToUnderlyingTokenRateType0.from_dict(
                    data
                )

                return pt_to_underlying_token_rate_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GetSpotSwappingPriceResponsePtToUnderlyingTokenRateType0", None], data)

        pt_to_underlying_token_rate = _parse_pt_to_underlying_token_rate(d.pop("ptToUnderlyingTokenRate"))

        def _parse_underlying_token_to_yt_rate(
            data: object,
        ) -> Union["GetSpotSwappingPriceResponseUnderlyingTokenToYtRateType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                underlying_token_to_yt_rate_type_0 = GetSpotSwappingPriceResponseUnderlyingTokenToYtRateType0.from_dict(
                    data
                )

                return underlying_token_to_yt_rate_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GetSpotSwappingPriceResponseUnderlyingTokenToYtRateType0", None], data)

        underlying_token_to_yt_rate = _parse_underlying_token_to_yt_rate(d.pop("underlyingTokenToYtRate"))

        def _parse_yt_to_underlying_token_rate(
            data: object,
        ) -> Union["GetSpotSwappingPriceResponseYtToUnderlyingTokenRateType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                yt_to_underlying_token_rate_type_0 = GetSpotSwappingPriceResponseYtToUnderlyingTokenRateType0.from_dict(
                    data
                )

                return yt_to_underlying_token_rate_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GetSpotSwappingPriceResponseYtToUnderlyingTokenRateType0", None], data)

        yt_to_underlying_token_rate = _parse_yt_to_underlying_token_rate(d.pop("ytToUnderlyingTokenRate"))

        implied_apy = d.pop("impliedApy")

        get_spot_swapping_price_response = cls(
            underlying_token=underlying_token,
            underlying_token_to_pt_rate=underlying_token_to_pt_rate,
            pt_to_underlying_token_rate=pt_to_underlying_token_rate,
            underlying_token_to_yt_rate=underlying_token_to_yt_rate,
            yt_to_underlying_token_rate=yt_to_underlying_token_rate,
            implied_apy=implied_apy,
        )

        get_spot_swapping_price_response.additional_properties = d
        return get_spot_swapping_price_response

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
