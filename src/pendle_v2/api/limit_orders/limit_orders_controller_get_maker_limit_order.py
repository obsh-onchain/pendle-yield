from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.limit_orders_controller_get_maker_limit_order_type import LimitOrdersControllerGetMakerLimitOrderType
from ...models.limit_orders_response import LimitOrdersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    chain_id: float,
    maker: str,
    yt: Union[Unset, str] = UNSET,
    type_: Union[Unset, LimitOrdersControllerGetMakerLimitOrderType] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["skip"] = skip

    params["limit"] = limit

    params["chainId"] = chain_id

    params["maker"] = maker

    params["yt"] = yt

    json_type_: Union[Unset, int] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["isActive"] = is_active

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/limit-orders/makers/limit-orders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[LimitOrdersResponse]:
    if response.status_code == 201:
        response_201 = LimitOrdersResponse.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[LimitOrdersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    chain_id: float,
    maker: str,
    yt: Union[Unset, str] = UNSET,
    type_: Union[Unset, LimitOrdersControllerGetMakerLimitOrderType] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
) -> Response[LimitOrdersResponse]:
    """Get user limit orders in market

     This endpoint let you fetch limit orders of a user in a market, it have more filter options than the
    analytics endpoint but have less item per page than the analytics endpoint.

    This limitation is more than enough for most use cases, given that a user can only have 50 orders
    per markets.

    Args:
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        chain_id (float):
        maker (str):
        yt (Union[Unset, str]):
        type_ (Union[Unset, LimitOrdersControllerGetMakerLimitOrderType]):
        is_active (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LimitOrdersResponse]
    """

    kwargs = _get_kwargs(
        skip=skip,
        limit=limit,
        chain_id=chain_id,
        maker=maker,
        yt=yt,
        type_=type_,
        is_active=is_active,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    chain_id: float,
    maker: str,
    yt: Union[Unset, str] = UNSET,
    type_: Union[Unset, LimitOrdersControllerGetMakerLimitOrderType] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
) -> Optional[LimitOrdersResponse]:
    """Get user limit orders in market

     This endpoint let you fetch limit orders of a user in a market, it have more filter options than the
    analytics endpoint but have less item per page than the analytics endpoint.

    This limitation is more than enough for most use cases, given that a user can only have 50 orders
    per markets.

    Args:
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        chain_id (float):
        maker (str):
        yt (Union[Unset, str]):
        type_ (Union[Unset, LimitOrdersControllerGetMakerLimitOrderType]):
        is_active (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LimitOrdersResponse
    """

    return sync_detailed(
        client=client,
        skip=skip,
        limit=limit,
        chain_id=chain_id,
        maker=maker,
        yt=yt,
        type_=type_,
        is_active=is_active,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    chain_id: float,
    maker: str,
    yt: Union[Unset, str] = UNSET,
    type_: Union[Unset, LimitOrdersControllerGetMakerLimitOrderType] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
) -> Response[LimitOrdersResponse]:
    """Get user limit orders in market

     This endpoint let you fetch limit orders of a user in a market, it have more filter options than the
    analytics endpoint but have less item per page than the analytics endpoint.

    This limitation is more than enough for most use cases, given that a user can only have 50 orders
    per markets.

    Args:
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        chain_id (float):
        maker (str):
        yt (Union[Unset, str]):
        type_ (Union[Unset, LimitOrdersControllerGetMakerLimitOrderType]):
        is_active (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LimitOrdersResponse]
    """

    kwargs = _get_kwargs(
        skip=skip,
        limit=limit,
        chain_id=chain_id,
        maker=maker,
        yt=yt,
        type_=type_,
        is_active=is_active,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    chain_id: float,
    maker: str,
    yt: Union[Unset, str] = UNSET,
    type_: Union[Unset, LimitOrdersControllerGetMakerLimitOrderType] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
) -> Optional[LimitOrdersResponse]:
    """Get user limit orders in market

     This endpoint let you fetch limit orders of a user in a market, it have more filter options than the
    analytics endpoint but have less item per page than the analytics endpoint.

    This limitation is more than enough for most use cases, given that a user can only have 50 orders
    per markets.

    Args:
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        chain_id (float):
        maker (str):
        yt (Union[Unset, str]):
        type_ (Union[Unset, LimitOrdersControllerGetMakerLimitOrderType]):
        is_active (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LimitOrdersResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            skip=skip,
            limit=limit,
            chain_id=chain_id,
            maker=maker,
            yt=yt,
            type_=type_,
            is_active=is_active,
        )
    ).parsed
