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
    aggregators: Union[Unset, str] = UNSET,
    tokens_in: str,
    amounts_in: str,
    tokens_out: str,
    redeem_rewards: Union[Unset, bool] = False,
    need_scale: Union[Unset, bool] = False,
    additional_data: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["receiver"] = receiver

    params["slippage"] = slippage

    params["enableAggregator"] = enable_aggregator

    params["aggregators"] = aggregators

    params["tokensIn"] = tokens_in

    params["amountsIn"] = amounts_in

    params["tokensOut"] = tokens_out

    params["redeemRewards"] = redeem_rewards

    params["needScale"] = need_scale

    params["additionalData"] = additional_data

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sdk/{chain_id}/convert",
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
    aggregators: Union[Unset, str] = UNSET,
    tokens_in: str,
    amounts_in: str,
    tokens_out: str,
    redeem_rewards: Union[Unset, bool] = False,
    need_scale: Union[Unset, bool] = False,
    additional_data: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Auto detect actions based on inputs and outputs

     Automatically identifies the action based on your input/output tokens. Supports swap, add-liquidity,
    remove-liquidity, add-liquidity-dual, remove-liquidity-dual, mint, redeem, mint-sy, redeem-sy,
    transfer-liquidity, roll-over-pt, and exit-positions.

    Args:
        chain_id (float):
        receiver (str):
        slippage (float):
        enable_aggregator (Union[Unset, bool]):  Default: False.
        aggregators (Union[Unset, str]):  Example: kyberswap,okx.
        tokens_in (str):
        amounts_in (str):
        tokens_out (str):
        redeem_rewards (Union[Unset, bool]):  Default: False.
        need_scale (Union[Unset, bool]):  Default: False.
        additional_data (Union[Unset, str]):

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
        aggregators=aggregators,
        tokens_in=tokens_in,
        amounts_in=amounts_in,
        tokens_out=tokens_out,
        redeem_rewards=redeem_rewards,
        need_scale=need_scale,
        additional_data=additional_data,
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
    aggregators: Union[Unset, str] = UNSET,
    tokens_in: str,
    amounts_in: str,
    tokens_out: str,
    redeem_rewards: Union[Unset, bool] = False,
    need_scale: Union[Unset, bool] = False,
    additional_data: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Auto detect actions based on inputs and outputs

     Automatically identifies the action based on your input/output tokens. Supports swap, add-liquidity,
    remove-liquidity, add-liquidity-dual, remove-liquidity-dual, mint, redeem, mint-sy, redeem-sy,
    transfer-liquidity, roll-over-pt, and exit-positions.

    Args:
        chain_id (float):
        receiver (str):
        slippage (float):
        enable_aggregator (Union[Unset, bool]):  Default: False.
        aggregators (Union[Unset, str]):  Example: kyberswap,okx.
        tokens_in (str):
        amounts_in (str):
        tokens_out (str):
        redeem_rewards (Union[Unset, bool]):  Default: False.
        need_scale (Union[Unset, bool]):  Default: False.
        additional_data (Union[Unset, str]):

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
        aggregators=aggregators,
        tokens_in=tokens_in,
        amounts_in=amounts_in,
        tokens_out=tokens_out,
        redeem_rewards=redeem_rewards,
        need_scale=need_scale,
        additional_data=additional_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
