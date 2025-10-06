from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain_id: float,
    *,
    receiver: str,
    slippage: float,
    enable_aggregator: Union[Unset, bool] = False,
    yt: str,
    token_in: str,
    amount_in: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["receiver"] = receiver

    params["slippage"] = slippage

    params["enableAggregator"] = enable_aggregator

    params["yt"] = yt

    params["tokenIn"] = token_in

    params["amountIn"] = amount_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/sdk/{chain_id}/mint",
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
    *,
    client: Union[AuthenticatedClient, Client],
    receiver: str,
    slippage: float,
    enable_aggregator: Union[Unset, bool] = False,
    yt: str,
    token_in: str,
    amount_in: str,
) -> Response[Any]:
    """Deprecated. Will be removed on 1st September 2025

    Args:
        chain_id (float):
        receiver (str):
        slippage (float):
        enable_aggregator (Union[Unset, bool]):  Default: False.
        yt (str):
        token_in (str):
        amount_in (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        receiver=receiver,
        slippage=slippage,
        enable_aggregator=enable_aggregator,
        yt=yt,
        token_in=token_in,
        amount_in=amount_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    chain_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
    receiver: str,
    slippage: float,
    enable_aggregator: Union[Unset, bool] = False,
    yt: str,
    token_in: str,
    amount_in: str,
) -> Response[Any]:
    """Deprecated. Will be removed on 1st September 2025

    Args:
        chain_id (float):
        receiver (str):
        slippage (float):
        enable_aggregator (Union[Unset, bool]):  Default: False.
        yt (str):
        token_in (str):
        amount_in (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chain_id=chain_id,
        receiver=receiver,
        slippage=slippage,
        enable_aggregator=enable_aggregator,
        yt=yt,
        token_in=token_in,
        amount_in=amount_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
