from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.limit_orders_response import LimitOrdersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    order_by: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 100.0,
    chain_id: Union[Unset, float] = UNSET,
    yt: Union[Unset, str] = UNSET,
    maker: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["order_by"] = order_by

    params["skip"] = skip

    params["limit"] = limit

    params["chainId"] = chain_id

    params["yt"] = yt

    params["maker"] = maker

    params["isActive"] = is_active

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/limit-orders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[LimitOrdersResponse]:
    if response.status_code == 200:
        response_200 = LimitOrdersResponse.from_dict(response.json())

        return response_200

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
    order_by: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 100.0,
    chain_id: Union[Unset, float] = UNSET,
    yt: Union[Unset, str] = UNSET,
    maker: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
) -> Response[LimitOrdersResponse]:
    """Get limit orders

     Deprecated, this is for pendle internal use only. Please use [this API](https://api-
    v2.pendle.finance/core/docs#/Limit%20Orders/LimitOrdersController_getAllLimitOrders) to fetch limit
    orders

    Args:
        order_by (Union[Unset, str]):  Example: latestEventTimestamp:-1.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 100.0.
        chain_id (Union[Unset, float]):
        yt (Union[Unset, str]):
        maker (Union[Unset, str]):
        is_active (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LimitOrdersResponse]
    """

    kwargs = _get_kwargs(
        order_by=order_by,
        skip=skip,
        limit=limit,
        chain_id=chain_id,
        yt=yt,
        maker=maker,
        is_active=is_active,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    order_by: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 100.0,
    chain_id: Union[Unset, float] = UNSET,
    yt: Union[Unset, str] = UNSET,
    maker: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
) -> Optional[LimitOrdersResponse]:
    """Get limit orders

     Deprecated, this is for pendle internal use only. Please use [this API](https://api-
    v2.pendle.finance/core/docs#/Limit%20Orders/LimitOrdersController_getAllLimitOrders) to fetch limit
    orders

    Args:
        order_by (Union[Unset, str]):  Example: latestEventTimestamp:-1.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 100.0.
        chain_id (Union[Unset, float]):
        yt (Union[Unset, str]):
        maker (Union[Unset, str]):
        is_active (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LimitOrdersResponse
    """

    return sync_detailed(
        client=client,
        order_by=order_by,
        skip=skip,
        limit=limit,
        chain_id=chain_id,
        yt=yt,
        maker=maker,
        is_active=is_active,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    order_by: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 100.0,
    chain_id: Union[Unset, float] = UNSET,
    yt: Union[Unset, str] = UNSET,
    maker: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
) -> Response[LimitOrdersResponse]:
    """Get limit orders

     Deprecated, this is for pendle internal use only. Please use [this API](https://api-
    v2.pendle.finance/core/docs#/Limit%20Orders/LimitOrdersController_getAllLimitOrders) to fetch limit
    orders

    Args:
        order_by (Union[Unset, str]):  Example: latestEventTimestamp:-1.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 100.0.
        chain_id (Union[Unset, float]):
        yt (Union[Unset, str]):
        maker (Union[Unset, str]):
        is_active (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LimitOrdersResponse]
    """

    kwargs = _get_kwargs(
        order_by=order_by,
        skip=skip,
        limit=limit,
        chain_id=chain_id,
        yt=yt,
        maker=maker,
        is_active=is_active,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    order_by: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 100.0,
    chain_id: Union[Unset, float] = UNSET,
    yt: Union[Unset, str] = UNSET,
    maker: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
) -> Optional[LimitOrdersResponse]:
    """Get limit orders

     Deprecated, this is for pendle internal use only. Please use [this API](https://api-
    v2.pendle.finance/core/docs#/Limit%20Orders/LimitOrdersController_getAllLimitOrders) to fetch limit
    orders

    Args:
        order_by (Union[Unset, str]):  Example: latestEventTimestamp:-1.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 100.0.
        chain_id (Union[Unset, float]):
        yt (Union[Unset, str]):
        maker (Union[Unset, str]):
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
            order_by=order_by,
            skip=skip,
            limit=limit,
            chain_id=chain_id,
            yt=yt,
            maker=maker,
            is_active=is_active,
        )
    ).parsed
