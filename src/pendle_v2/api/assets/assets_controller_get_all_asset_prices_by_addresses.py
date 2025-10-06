from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_asset_prices_response import GetAssetPricesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain_id: float,
    *,
    addresses: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["addresses"] = addresses

    params["skip"] = skip

    params["limit"] = limit

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/{chain_id}/assets/prices",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetAssetPricesResponse]:
    if response.status_code == 200:
        response_200 = GetAssetPricesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetAssetPricesResponse]:
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
    addresses: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[GetAssetPricesResponse]:
    """Get asset prices

     USD prices for specific assets. Updated every minute. For real-time prices, use the swapping-price
    endpoint.

    Args:
        chain_id (float):
        addresses (Union[Unset, str]):  Example:
            0x5fe30ac5cb1abb0e44cdffb2916c254aeb368650,0xc5cd692e9b4622ab8cdb57c83a0f99f874a169cd.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAssetPricesResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        addresses=addresses,
        skip=skip,
        limit=limit,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    addresses: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Optional[GetAssetPricesResponse]:
    """Get asset prices

     USD prices for specific assets. Updated every minute. For real-time prices, use the swapping-price
    endpoint.

    Args:
        chain_id (float):
        addresses (Union[Unset, str]):  Example:
            0x5fe30ac5cb1abb0e44cdffb2916c254aeb368650,0xc5cd692e9b4622ab8cdb57c83a0f99f874a169cd.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAssetPricesResponse
    """

    return sync_detailed(
        chain_id=chain_id,
        client=client,
        addresses=addresses,
        skip=skip,
        limit=limit,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    addresses: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[GetAssetPricesResponse]:
    """Get asset prices

     USD prices for specific assets. Updated every minute. For real-time prices, use the swapping-price
    endpoint.

    Args:
        chain_id (float):
        addresses (Union[Unset, str]):  Example:
            0x5fe30ac5cb1abb0e44cdffb2916c254aeb368650,0xc5cd692e9b4622ab8cdb57c83a0f99f874a169cd.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAssetPricesResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        addresses=addresses,
        skip=skip,
        limit=limit,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    addresses: Union[Unset, str] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Optional[GetAssetPricesResponse]:
    """Get asset prices

     USD prices for specific assets. Updated every minute. For real-time prices, use the swapping-price
    endpoint.

    Args:
        chain_id (float):
        addresses (Union[Unset, str]):  Example:
            0x5fe30ac5cb1abb0e44cdffb2916c254aeb368650,0xc5cd692e9b4622ab8cdb57c83a0f99f874a169cd.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAssetPricesResponse
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            client=client,
            addresses=addresses,
            skip=skip,
            limit=limit,
            type_=type_,
        )
    ).parsed
