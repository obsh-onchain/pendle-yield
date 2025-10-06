from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    chain_id: float,
    market: str,
    *,
    receiver: str,
    slippage: float,
    token_in: str,
    amount_token_in: str,
    amount_pt_in: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["receiver"] = receiver

    params["slippage"] = slippage

    params["tokenIn"] = token_in

    params["amountTokenIn"] = amount_token_in

    params["amountPtIn"] = amount_pt_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/sdk/{chain_id}/markets/{market}/add-liquidity-dual",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    receiver: str,
    slippage: float,
    token_in: str,
    amount_token_in: str,
    amount_pt_in: str,
) -> Response[Any]:
    """Dual liquidity provision, using both tokens and PT

     Dual liquidity provision, using both tokens and PT. Only callable until market's expiry.

    Args:
        chain_id (float):
        market (str):
        receiver (str):
        slippage (float):
        token_in (str):
        amount_token_in (str):
        amount_pt_in (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        market=market,
        receiver=receiver,
        slippage=slippage,
        token_in=token_in,
        amount_token_in=amount_token_in,
        amount_pt_in=amount_pt_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    chain_id: float,
    market: str,
    *,
    client: Union[AuthenticatedClient, Client],
    receiver: str,
    slippage: float,
    token_in: str,
    amount_token_in: str,
    amount_pt_in: str,
) -> Response[Any]:
    """Dual liquidity provision, using both tokens and PT

     Dual liquidity provision, using both tokens and PT. Only callable until market's expiry.

    Args:
        chain_id (float):
        market (str):
        receiver (str):
        slippage (float):
        token_in (str):
        amount_token_in (str):
        amount_pt_in (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        market=market,
        receiver=receiver,
        slippage=slippage,
        token_in=token_in,
        amount_token_in=amount_token_in,
        amount_pt_in=amount_pt_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
