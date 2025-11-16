from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.swap_amount_to_change_apy_response import SwapAmountToChangeApyResponse
from ...types import UNSET, Response


def _get_kwargs(
    chain_id: float,
    address: str,
    *,
    token_in: str,
    token_out: str,
    target_implied_apy: float,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["tokenIn"] = token_in

    params["tokenOut"] = token_out

    params["targetImpliedApy"] = target_implied_apy

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/{chain_id}/markets/{address}/swap-amount-to-change-implied-apy",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SwapAmountToChangeApyResponse]:
    if response.status_code == 200:
        response_200 = SwapAmountToChangeApyResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SwapAmountToChangeApyResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    token_in: str,
    token_out: str,
    target_implied_apy: float,
) -> Response[SwapAmountToChangeApyResponse]:
    """Get market liquidity depth by address

     Get the amount required to swap in the market to change the implied apy to a given target, including
    liquidity from order books and AMM

    Args:
        chain_id (float):
        address (str):
        token_in (str):
        token_out (str):
        target_implied_apy (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SwapAmountToChangeApyResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        address=address,
        token_in=token_in,
        token_out=token_out,
        target_implied_apy=target_implied_apy,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    token_in: str,
    token_out: str,
    target_implied_apy: float,
) -> Optional[SwapAmountToChangeApyResponse]:
    """Get market liquidity depth by address

     Get the amount required to swap in the market to change the implied apy to a given target, including
    liquidity from order books and AMM

    Args:
        chain_id (float):
        address (str):
        token_in (str):
        token_out (str):
        target_implied_apy (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SwapAmountToChangeApyResponse
    """

    return sync_detailed(
        chain_id=chain_id,
        address=address,
        client=client,
        token_in=token_in,
        token_out=token_out,
        target_implied_apy=target_implied_apy,
    ).parsed


async def asyncio_detailed(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    token_in: str,
    token_out: str,
    target_implied_apy: float,
) -> Response[SwapAmountToChangeApyResponse]:
    """Get market liquidity depth by address

     Get the amount required to swap in the market to change the implied apy to a given target, including
    liquidity from order books and AMM

    Args:
        chain_id (float):
        address (str):
        token_in (str):
        token_out (str):
        target_implied_apy (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SwapAmountToChangeApyResponse]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        address=address,
        token_in=token_in,
        token_out=token_out,
        target_implied_apy=target_implied_apy,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain_id: float,
    address: str,
    *,
    client: Union[AuthenticatedClient, Client],
    token_in: str,
    token_out: str,
    target_implied_apy: float,
) -> Optional[SwapAmountToChangeApyResponse]:
    """Get market liquidity depth by address

     Get the amount required to swap in the market to change the implied apy to a given target, including
    liquidity from order books and AMM

    Args:
        chain_id (float):
        address (str):
        token_in (str):
        token_out (str):
        target_implied_apy (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SwapAmountToChangeApyResponse
    """

    return (
        await asyncio_detailed(
            chain_id=chain_id,
            address=address,
            client=client,
            token_in=token_in,
            token_out=token_out,
            target_implied_apy=target_implied_apy,
        )
    ).parsed
