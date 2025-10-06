from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.uniswap_token_list_response import UniswapTokenListResponse
from ...types import Response


def _get_kwargs(
    chain_id: float,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/{chain_id}/assets/pendle-token/list",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UniswapTokenListResponse]:
    if response.status_code == 200:
        response_200 = UniswapTokenListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UniswapTokenListResponse]:
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
) -> Response[UniswapTokenListResponse]:
    """Get Pendle tokens in Uniswap format

     Token list compatible with Uniswap interface, following the standard token list schema.

    Args:
        chain_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UniswapTokenListResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[UniswapTokenListResponse]:
    """Get Pendle tokens in Uniswap format

     Token list compatible with Uniswap interface, following the standard token list schema.

    Args:
        chain_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UniswapTokenListResponse
    """

    return sync_detailed(
        chain_id=chain_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[UniswapTokenListResponse]:
    """Get Pendle tokens in Uniswap format

     Token list compatible with Uniswap interface, following the standard token list schema.

    Args:
        chain_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UniswapTokenListResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[UniswapTokenListResponse]:
    """Get Pendle tokens in Uniswap format

     Token list compatible with Uniswap interface, following the standard token list schema.

    Args:
        chain_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UniswapTokenListResponse
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            client=client,
        )
    ).parsed
