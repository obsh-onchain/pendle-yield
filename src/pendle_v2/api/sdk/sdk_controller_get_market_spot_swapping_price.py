from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_spot_swapping_price_response import GetSpotSwappingPriceResponse
from ...types import Response


def _get_kwargs(
    chain_id: float,
    market: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/sdk/{chain_id}/markets/{market}/swapping-prices",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetSpotSwappingPriceResponse]:
    if response.status_code == 200:
        response_200 = GetSpotSwappingPriceResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetSpotSwappingPriceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chain_id: float,
    market: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetSpotSwappingPriceResponse]:
    """Get real-time PT/YT swap price of a market

     Return price by swapping  1 unit underlying token to PT/ YT, and 1 unit of PT/YT to the underlying
    token.

    One unit is defined as 10**decimal. The result is updated every block.

    Implied APY of the market is also included.

    Args:
        chain_id (float):
        market (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSpotSwappingPriceResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        market=market,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain_id: float,
    market: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetSpotSwappingPriceResponse]:
    """Get real-time PT/YT swap price of a market

     Return price by swapping  1 unit underlying token to PT/ YT, and 1 unit of PT/YT to the underlying
    token.

    One unit is defined as 10**decimal. The result is updated every block.

    Implied APY of the market is also included.

    Args:
        chain_id (float):
        market (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSpotSwappingPriceResponse
    """

    return sync_detailed(
        chain_id=chain_id,
        market=market,
        client=client,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    market: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetSpotSwappingPriceResponse]:
    """Get real-time PT/YT swap price of a market

     Return price by swapping  1 unit underlying token to PT/ YT, and 1 unit of PT/YT to the underlying
    token.

    One unit is defined as 10**decimal. The result is updated every block.

    Implied APY of the market is also included.

    Args:
        chain_id (float):
        market (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSpotSwappingPriceResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        market=market,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    market: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetSpotSwappingPriceResponse]:
    """Get real-time PT/YT swap price of a market

     Return price by swapping  1 unit underlying token to PT/ YT, and 1 unit of PT/YT to the underlying
    token.

    One unit is defined as 10**decimal. The result is updated every block.

    Implied APY of the market is also included.

    Args:
        chain_id (float):
        market (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSpotSwappingPriceResponse
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            market=market,
            client=client,
        )
    ).parsed
