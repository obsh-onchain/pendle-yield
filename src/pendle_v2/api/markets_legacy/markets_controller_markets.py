from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.markets_response import MarketsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain_id: float,
    *,
    order_by: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    is_expired: Union[Unset, bool] = UNSET,
    select: Union[Unset, str] = UNSET,
    pt: Union[Unset, str] = UNSET,
    yt: Union[Unset, str] = UNSET,
    sy: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    category_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["order_by"] = order_by

    params["skip"] = skip

    params["limit"] = limit

    params["is_expired"] = is_expired

    params["select"] = select

    params["pt"] = pt

    params["yt"] = yt

    params["sy"] = sy

    params["q"] = q

    params["is_active"] = is_active

    params["categoryId"] = category_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/{chain_id}/markets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MarketsResponse]:
    if response.status_code == 200:
        response_200 = MarketsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MarketsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    order_by: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    is_expired: Union[Unset, bool] = UNSET,
    select: Union[Unset, str] = UNSET,
    pt: Union[Unset, str] = UNSET,
    yt: Union[Unset, str] = UNSET,
    sy: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    category_id: Union[Unset, str] = UNSET,
) -> Response[MarketsResponse]:
    """Get markets

    Args:
        chain_id (float):
        order_by (Union[Unset, str]):  Example: name:1.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        is_expired (Union[Unset, bool]):
        select (Union[Unset, str]):
        pt (Union[Unset, str]):
        yt (Union[Unset, str]):
        sy (Union[Unset, str]):
        q (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        category_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarketsResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        order_by=order_by,
        skip=skip,
        limit=limit,
        is_expired=is_expired,
        select=select,
        pt=pt,
        yt=yt,
        sy=sy,
        q=q,
        is_active=is_active,
        category_id=category_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    order_by: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    is_expired: Union[Unset, bool] = UNSET,
    select: Union[Unset, str] = UNSET,
    pt: Union[Unset, str] = UNSET,
    yt: Union[Unset, str] = UNSET,
    sy: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    category_id: Union[Unset, str] = UNSET,
) -> Optional[MarketsResponse]:
    """Get markets

    Args:
        chain_id (float):
        order_by (Union[Unset, str]):  Example: name:1.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        is_expired (Union[Unset, bool]):
        select (Union[Unset, str]):
        pt (Union[Unset, str]):
        yt (Union[Unset, str]):
        sy (Union[Unset, str]):
        q (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        category_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarketsResponse
    """

    return sync_detailed(
        chain_id=chain_id,
        client=client,
        order_by=order_by,
        skip=skip,
        limit=limit,
        is_expired=is_expired,
        select=select,
        pt=pt,
        yt=yt,
        sy=sy,
        q=q,
        is_active=is_active,
        category_id=category_id,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    order_by: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    is_expired: Union[Unset, bool] = UNSET,
    select: Union[Unset, str] = UNSET,
    pt: Union[Unset, str] = UNSET,
    yt: Union[Unset, str] = UNSET,
    sy: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    category_id: Union[Unset, str] = UNSET,
) -> Response[MarketsResponse]:
    """Get markets

    Args:
        chain_id (float):
        order_by (Union[Unset, str]):  Example: name:1.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        is_expired (Union[Unset, bool]):
        select (Union[Unset, str]):
        pt (Union[Unset, str]):
        yt (Union[Unset, str]):
        sy (Union[Unset, str]):
        q (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        category_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarketsResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        order_by=order_by,
        skip=skip,
        limit=limit,
        is_expired=is_expired,
        select=select,
        pt=pt,
        yt=yt,
        sy=sy,
        q=q,
        is_active=is_active,
        category_id=category_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    order_by: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    is_expired: Union[Unset, bool] = UNSET,
    select: Union[Unset, str] = UNSET,
    pt: Union[Unset, str] = UNSET,
    yt: Union[Unset, str] = UNSET,
    sy: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    category_id: Union[Unset, str] = UNSET,
) -> Optional[MarketsResponse]:
    """Get markets

    Args:
        chain_id (float):
        order_by (Union[Unset, str]):  Example: name:1.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        is_expired (Union[Unset, bool]):
        select (Union[Unset, str]):
        pt (Union[Unset, str]):
        yt (Union[Unset, str]):
        sy (Union[Unset, str]):
        q (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        category_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarketsResponse
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            client=client,
            order_by=order_by,
            skip=skip,
            limit=limit,
            is_expired=is_expired,
            select=select,
            pt=pt,
            yt=yt,
            sy=sy,
            q=q,
            is_active=is_active,
            category_id=category_id,
        )
    ).parsed
