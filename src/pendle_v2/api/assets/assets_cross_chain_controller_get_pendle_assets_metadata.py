from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_assets_cross_chain_response import GetAllAssetsCrossChainResponse
from ...models.pendle_asset_type import PendleAssetType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: Union[Unset, str] = UNSET,
    chain_id: Union[Unset, float] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = UNSET,
    type_: Union[Unset, PendleAssetType] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ids"] = ids

    params["chainId"] = chain_id

    params["skip"] = skip

    params["limit"] = limit

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/all",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetAllAssetsCrossChainResponse]:
    if response.status_code == 200:
        response_200 = GetAllAssetsCrossChainResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetAllAssetsCrossChainResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ids: Union[Unset, str] = UNSET,
    chain_id: Union[Unset, float] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = UNSET,
    type_: Union[Unset, PendleAssetType] = UNSET,
) -> Response[GetAllAssetsCrossChainResponse]:
    """Get supported PT, YT, LP, SY assets

     Returns list of PT, YT, LP, SY assets supported in Pendle App, including: name, symbol, address,
    decimals, expiry (if applicable), icon.

    Can filter by chain id, asset id, asset type.

    Price are not included in the response.

    Args:
        ids (Union[Unset, str]):  Example:
            1-0x5fe30ac5cb1abb0e44cdffb2916c254aeb368650,1-0xc5cd692e9b4622ab8cdb57c83a0f99f874a169cd.
        chain_id (Union[Unset, float]):  Example: 1.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):
        type_ (Union[Unset, PendleAssetType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllAssetsCrossChainResponse]
    """

    kwargs = _get_kwargs(
        ids=ids,
        chain_id=chain_id,
        skip=skip,
        limit=limit,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    ids: Union[Unset, str] = UNSET,
    chain_id: Union[Unset, float] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = UNSET,
    type_: Union[Unset, PendleAssetType] = UNSET,
) -> Optional[GetAllAssetsCrossChainResponse]:
    """Get supported PT, YT, LP, SY assets

     Returns list of PT, YT, LP, SY assets supported in Pendle App, including: name, symbol, address,
    decimals, expiry (if applicable), icon.

    Can filter by chain id, asset id, asset type.

    Price are not included in the response.

    Args:
        ids (Union[Unset, str]):  Example:
            1-0x5fe30ac5cb1abb0e44cdffb2916c254aeb368650,1-0xc5cd692e9b4622ab8cdb57c83a0f99f874a169cd.
        chain_id (Union[Unset, float]):  Example: 1.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):
        type_ (Union[Unset, PendleAssetType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllAssetsCrossChainResponse
    """

    return sync_detailed(
        client=client,
        ids=ids,
        chain_id=chain_id,
        skip=skip,
        limit=limit,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ids: Union[Unset, str] = UNSET,
    chain_id: Union[Unset, float] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = UNSET,
    type_: Union[Unset, PendleAssetType] = UNSET,
) -> Response[GetAllAssetsCrossChainResponse]:
    """Get supported PT, YT, LP, SY assets

     Returns list of PT, YT, LP, SY assets supported in Pendle App, including: name, symbol, address,
    decimals, expiry (if applicable), icon.

    Can filter by chain id, asset id, asset type.

    Price are not included in the response.

    Args:
        ids (Union[Unset, str]):  Example:
            1-0x5fe30ac5cb1abb0e44cdffb2916c254aeb368650,1-0xc5cd692e9b4622ab8cdb57c83a0f99f874a169cd.
        chain_id (Union[Unset, float]):  Example: 1.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):
        type_ (Union[Unset, PendleAssetType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllAssetsCrossChainResponse]
    """

    kwargs = _get_kwargs(
        ids=ids,
        chain_id=chain_id,
        skip=skip,
        limit=limit,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    ids: Union[Unset, str] = UNSET,
    chain_id: Union[Unset, float] = UNSET,
    skip: Union[Unset, float] = 0.0,
    limit: Union[Unset, float] = UNSET,
    type_: Union[Unset, PendleAssetType] = UNSET,
) -> Optional[GetAllAssetsCrossChainResponse]:
    """Get supported PT, YT, LP, SY assets

     Returns list of PT, YT, LP, SY assets supported in Pendle App, including: name, symbol, address,
    decimals, expiry (if applicable), icon.

    Can filter by chain id, asset id, asset type.

    Price are not included in the response.

    Args:
        ids (Union[Unset, str]):  Example:
            1-0x5fe30ac5cb1abb0e44cdffb2916c254aeb368650,1-0xc5cd692e9b4622ab8cdb57c83a0f99f874a169cd.
        chain_id (Union[Unset, float]):  Example: 1.
        skip (Union[Unset, float]):  Default: 0.0.
        limit (Union[Unset, float]):
        type_ (Union[Unset, PendleAssetType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllAssetsCrossChainResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            chain_id=chain_id,
            skip=skip,
            limit=limit,
            type_=type_,
        )
    ).parsed
