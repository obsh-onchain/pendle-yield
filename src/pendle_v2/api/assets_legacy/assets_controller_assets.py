from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assets_response import AssetsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain_id: float,
    *,
    order_by: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    is_expired: Union[Unset, bool] = UNSET,
    zappable: Union[Unset, bool] = UNSET,
    type_: Union[Unset, str] = UNSET,
    address: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["order_by"] = order_by

    params["skip"] = skip

    params["limit"] = limit

    params["is_expired"] = is_expired

    params["zappable"] = zappable

    params["type"] = type_

    params["address"] = address

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/{chain_id}/assets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AssetsResponse]:
    if response.status_code == 200:
        response_200 = AssetsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AssetsResponse]:
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
    zappable: Union[Unset, bool] = UNSET,
    type_: Union[Unset, str] = UNSET,
    address: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
) -> Response[AssetsResponse]:
    """Get assets with filters

    Args:
        chain_id (float):
        order_by (Union[Unset, str]):  Example: name:1.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        is_expired (Union[Unset, bool]):
        zappable (Union[Unset, bool]):
        type_ (Union[Unset, str]):
        address (Union[Unset, str]):
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetsResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        order_by=order_by,
        skip=skip,
        limit=limit,
        is_expired=is_expired,
        zappable=zappable,
        type_=type_,
        address=address,
        q=q,
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
    zappable: Union[Unset, bool] = UNSET,
    type_: Union[Unset, str] = UNSET,
    address: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
) -> Optional[AssetsResponse]:
    """Get assets with filters

    Args:
        chain_id (float):
        order_by (Union[Unset, str]):  Example: name:1.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        is_expired (Union[Unset, bool]):
        zappable (Union[Unset, bool]):
        type_ (Union[Unset, str]):
        address (Union[Unset, str]):
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetsResponse
    """

    return sync_detailed(
        chain_id=chain_id,
        client=client,
        order_by=order_by,
        skip=skip,
        limit=limit,
        is_expired=is_expired,
        zappable=zappable,
        type_=type_,
        address=address,
        q=q,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    order_by: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = 10.0,
    is_expired: Union[Unset, bool] = UNSET,
    zappable: Union[Unset, bool] = UNSET,
    type_: Union[Unset, str] = UNSET,
    address: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
) -> Response[AssetsResponse]:
    """Get assets with filters

    Args:
        chain_id (float):
        order_by (Union[Unset, str]):  Example: name:1.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        is_expired (Union[Unset, bool]):
        zappable (Union[Unset, bool]):
        type_ (Union[Unset, str]):
        address (Union[Unset, str]):
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetsResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        order_by=order_by,
        skip=skip,
        limit=limit,
        is_expired=is_expired,
        zappable=zappable,
        type_=type_,
        address=address,
        q=q,
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
    zappable: Union[Unset, bool] = UNSET,
    type_: Union[Unset, str] = UNSET,
    address: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
) -> Optional[AssetsResponse]:
    """Get assets with filters

    Args:
        chain_id (float):
        order_by (Union[Unset, str]):  Example: name:1.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):  Default: 10.0.
        is_expired (Union[Unset, bool]):
        zappable (Union[Unset, bool]):
        type_ (Union[Unset, str]):
        address (Union[Unset, str]):
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetsResponse
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            client=client,
            order_by=order_by,
            skip=skip,
            limit=limit,
            is_expired=is_expired,
            zappable=zappable,
            type_=type_,
            address=address,
            q=q,
        )
    ).parsed
