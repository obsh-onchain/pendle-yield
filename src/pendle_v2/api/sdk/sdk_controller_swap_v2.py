from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain_id: float,
    market: str,
    *,
    receiver: str,
    slippage: float,
    enable_aggregator: Union[Unset, bool] = False,
    aggregators: Union[Unset, str] = UNSET,
    token_in: str,
    token_out: str,
    amount_in: str,
    additional_data: Union[Unset, str] = UNSET,
    need_scale: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["receiver"] = receiver

    params["slippage"] = slippage

    params["enableAggregator"] = enable_aggregator

    params["aggregators"] = aggregators

    params["tokenIn"] = token_in

    params["tokenOut"] = token_out

    params["amountIn"] = amount_in

    params["additionalData"] = additional_data

    params["needScale"] = need_scale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sdk/{chain_id}/markets/{market}/swap",
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
    enable_aggregator: Union[Unset, bool] = False,
    aggregators: Union[Unset, str] = UNSET,
    token_in: str,
    token_out: str,
    amount_in: str,
    additional_data: Union[Unset, str] = UNSET,
    need_scale: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Swap between tokens and PT/YT

     Swap between tokens and PT/YT. Only callable until the market's expiry.Swapping between PT and YT is
    not supported.

    Args:
        chain_id (float):
        market (str):
        receiver (str):
        slippage (float):
        enable_aggregator (Union[Unset, bool]):  Default: False.
        aggregators (Union[Unset, str]):  Example: kyberswap,okx.
        token_in (str):
        token_out (str):
        amount_in (str):
        additional_data (Union[Unset, str]):
        need_scale (Union[Unset, bool]):

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
        enable_aggregator=enable_aggregator,
        aggregators=aggregators,
        token_in=token_in,
        token_out=token_out,
        amount_in=amount_in,
        additional_data=additional_data,
        need_scale=need_scale,
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
    enable_aggregator: Union[Unset, bool] = False,
    aggregators: Union[Unset, str] = UNSET,
    token_in: str,
    token_out: str,
    amount_in: str,
    additional_data: Union[Unset, str] = UNSET,
    need_scale: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Swap between tokens and PT/YT

     Swap between tokens and PT/YT. Only callable until the market's expiry.Swapping between PT and YT is
    not supported.

    Args:
        chain_id (float):
        market (str):
        receiver (str):
        slippage (float):
        enable_aggregator (Union[Unset, bool]):  Default: False.
        aggregators (Union[Unset, str]):  Example: kyberswap,okx.
        token_in (str):
        token_out (str):
        amount_in (str):
        additional_data (Union[Unset, str]):
        need_scale (Union[Unset, bool]):

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
        enable_aggregator=enable_aggregator,
        aggregators=aggregators,
        token_in=token_in,
        token_out=token_out,
        amount_in=amount_in,
        additional_data=additional_data,
        need_scale=need_scale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
