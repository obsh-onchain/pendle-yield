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
    aggregators: Union[Unset, str] = UNSET,
    dst_market: str,
    lp_amount: str,
    pt_amount: str,
    yt_amount: str,
    redeem_rewards: Union[Unset, bool] = False,
    zpi: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["receiver"] = receiver

    params["slippage"] = slippage

    params["aggregators"] = aggregators

    params["dstMarket"] = dst_market

    params["lpAmount"] = lp_amount

    params["ptAmount"] = pt_amount

    params["ytAmount"] = yt_amount

    params["redeemRewards"] = redeem_rewards

    params["zpi"] = zpi

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/sdk/{chain_id}/markets/{market}/transfer-liquidity",
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
    aggregators: Union[Unset, str] = UNSET,
    dst_market: str,
    lp_amount: str,
    pt_amount: str,
    yt_amount: str,
    redeem_rewards: Union[Unset, bool] = False,
    zpi: Union[Unset, bool] = False,
) -> Response[Any]:
    """Transfer liquidity from one market to another

     Transfer liquidity from one market to another. All provided inputs (LP, PT & YT) will be
    sold/redeemed to the underlying asset before being zapped into the destination market. May not be
    possible for certain pairs of markets. Callable regardless of the market's expiry.

    Args:
        chain_id (float):
        market (str):
        receiver (str):
        slippage (float):
        aggregators (Union[Unset, str]):  Example: kyberswap,okx.
        dst_market (str):
        lp_amount (str):
        pt_amount (str):
        yt_amount (str):
        redeem_rewards (Union[Unset, bool]):  Default: False.
        zpi (Union[Unset, bool]):  Default: False.

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
        aggregators=aggregators,
        dst_market=dst_market,
        lp_amount=lp_amount,
        pt_amount=pt_amount,
        yt_amount=yt_amount,
        redeem_rewards=redeem_rewards,
        zpi=zpi,
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
    aggregators: Union[Unset, str] = UNSET,
    dst_market: str,
    lp_amount: str,
    pt_amount: str,
    yt_amount: str,
    redeem_rewards: Union[Unset, bool] = False,
    zpi: Union[Unset, bool] = False,
) -> Response[Any]:
    """Transfer liquidity from one market to another

     Transfer liquidity from one market to another. All provided inputs (LP, PT & YT) will be
    sold/redeemed to the underlying asset before being zapped into the destination market. May not be
    possible for certain pairs of markets. Callable regardless of the market's expiry.

    Args:
        chain_id (float):
        market (str):
        receiver (str):
        slippage (float):
        aggregators (Union[Unset, str]):  Example: kyberswap,okx.
        dst_market (str):
        lp_amount (str):
        pt_amount (str):
        yt_amount (str):
        redeem_rewards (Union[Unset, bool]):  Default: False.
        zpi (Union[Unset, bool]):  Default: False.

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
        aggregators=aggregators,
        dst_market=dst_market,
        lp_amount=lp_amount,
        pt_amount=pt_amount,
        yt_amount=yt_amount,
        redeem_rewards=redeem_rewards,
        zpi=zpi,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
