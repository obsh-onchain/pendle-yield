from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_markets_cross_chain_response import GetMarketsCrossChainResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    is_active: Union[Unset, bool] = UNSET,
    chain_id: Union[Unset, float] = UNSET,
    ids: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["isActive"] = is_active

    params["chainId"] = chain_id

    params["ids"] = ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/markets/all",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetMarketsCrossChainResponse]:
    if response.status_code == 200:
        response_200 = GetMarketsCrossChainResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetMarketsCrossChainResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    is_active: Union[Unset, bool] = UNSET,
    chain_id: Union[Unset, float] = UNSET,
    ids: Union[Unset, str] = UNSET,
) -> Response[GetMarketsCrossChainResponse]:
    """Get whitelisted markets list

     Get whitelisted markets list with its metadata across all chains.

    The data returns contains: market name, expiry, yt/pt/sy addresses, liquidity, trading volume,
    underlying apy, swap fee APY, pendle APY, fee rate, yield range, total pt, total sy in market, total
    supply of LP token, lp wrapper address (if applicable), etc.

    You can use chainId, isActive or ids params to filter markets.

    Args:
        is_active (Union[Unset, bool]):
        chain_id (Union[Unset, float]):
        ids (Union[Unset, str]):  Example:
            1-0x7b246b8dbc2a640bf2d8221890cee8327fc23917,1-0x44474d98d1484c26e8d296a43a721998731cf775.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMarketsCrossChainResponse]
    """

    kwargs = _get_kwargs(
        is_active=is_active,
        chain_id=chain_id,
        ids=ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    is_active: Union[Unset, bool] = UNSET,
    chain_id: Union[Unset, float] = UNSET,
    ids: Union[Unset, str] = UNSET,
) -> Optional[GetMarketsCrossChainResponse]:
    """Get whitelisted markets list

     Get whitelisted markets list with its metadata across all chains.

    The data returns contains: market name, expiry, yt/pt/sy addresses, liquidity, trading volume,
    underlying apy, swap fee APY, pendle APY, fee rate, yield range, total pt, total sy in market, total
    supply of LP token, lp wrapper address (if applicable), etc.

    You can use chainId, isActive or ids params to filter markets.

    Args:
        is_active (Union[Unset, bool]):
        chain_id (Union[Unset, float]):
        ids (Union[Unset, str]):  Example:
            1-0x7b246b8dbc2a640bf2d8221890cee8327fc23917,1-0x44474d98d1484c26e8d296a43a721998731cf775.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMarketsCrossChainResponse
    """

    return sync_detailed(
        client=client,
        is_active=is_active,
        chain_id=chain_id,
        ids=ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    is_active: Union[Unset, bool] = UNSET,
    chain_id: Union[Unset, float] = UNSET,
    ids: Union[Unset, str] = UNSET,
) -> Response[GetMarketsCrossChainResponse]:
    """Get whitelisted markets list

     Get whitelisted markets list with its metadata across all chains.

    The data returns contains: market name, expiry, yt/pt/sy addresses, liquidity, trading volume,
    underlying apy, swap fee APY, pendle APY, fee rate, yield range, total pt, total sy in market, total
    supply of LP token, lp wrapper address (if applicable), etc.

    You can use chainId, isActive or ids params to filter markets.

    Args:
        is_active (Union[Unset, bool]):
        chain_id (Union[Unset, float]):
        ids (Union[Unset, str]):  Example:
            1-0x7b246b8dbc2a640bf2d8221890cee8327fc23917,1-0x44474d98d1484c26e8d296a43a721998731cf775.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMarketsCrossChainResponse]
    """

    kwargs = _get_kwargs(
        is_active=is_active,
        chain_id=chain_id,
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    is_active: Union[Unset, bool] = UNSET,
    chain_id: Union[Unset, float] = UNSET,
    ids: Union[Unset, str] = UNSET,
) -> Optional[GetMarketsCrossChainResponse]:
    """Get whitelisted markets list

     Get whitelisted markets list with its metadata across all chains.

    The data returns contains: market name, expiry, yt/pt/sy addresses, liquidity, trading volume,
    underlying apy, swap fee APY, pendle APY, fee rate, yield range, total pt, total sy in market, total
    supply of LP token, lp wrapper address (if applicable), etc.

    You can use chainId, isActive or ids params to filter markets.

    Args:
        is_active (Union[Unset, bool]):
        chain_id (Union[Unset, float]):
        ids (Union[Unset, str]):  Example:
            1-0x7b246b8dbc2a640bf2d8221890cee8327fc23917,1-0x44474d98d1484c26e8d296a43a721998731cf775.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMarketsCrossChainResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            is_active=is_active,
            chain_id=chain_id,
            ids=ids,
        )
    ).parsed
