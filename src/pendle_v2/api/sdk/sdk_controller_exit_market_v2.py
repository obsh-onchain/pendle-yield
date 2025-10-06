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
    pt_amount: str,
    yt_amount: str,
    lp_amount: str,
    token_out: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["receiver"] = receiver

    params["slippage"] = slippage

    params["enableAggregator"] = enable_aggregator

    params["aggregators"] = aggregators

    params["ptAmount"] = pt_amount

    params["ytAmount"] = yt_amount

    params["lpAmount"] = lp_amount

    params["tokenOut"] = token_out

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sdk/{chain_id}/markets/{market}/exit-positions",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None

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
    pt_amount: str,
    yt_amount: str,
    lp_amount: str,
    token_out: str,
) -> Response[Any]:
    """Exit LP, PT and YT positions in a market to token/SY

     Exit LP, PT and YT positions in a market to token/SY

    Args:
        chain_id (float):
        market (str):
        receiver (str):
        slippage (float):
        enable_aggregator (Union[Unset, bool]):  Default: False.
        aggregators (Union[Unset, str]):  Example: kyberswap,okx.
        pt_amount (str):
        yt_amount (str):
        lp_amount (str):
        token_out (str):

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
        pt_amount=pt_amount,
        yt_amount=yt_amount,
        lp_amount=lp_amount,
        token_out=token_out,
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
    pt_amount: str,
    yt_amount: str,
    lp_amount: str,
    token_out: str,
) -> Response[Any]:
    """Exit LP, PT and YT positions in a market to token/SY

     Exit LP, PT and YT positions in a market to token/SY

    Args:
        chain_id (float):
        market (str):
        receiver (str):
        slippage (float):
        enable_aggregator (Union[Unset, bool]):  Default: False.
        aggregators (Union[Unset, str]):  Example: kyberswap,okx.
        pt_amount (str):
        yt_amount (str):
        lp_amount (str):
        token_out (str):

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
        pt_amount=pt_amount,
        yt_amount=yt_amount,
        lp_amount=lp_amount,
        token_out=token_out,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
